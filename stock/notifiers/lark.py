"""Send messages to Lark via official SDK."""

import os
import json
import lark_oapi as lark
from lark_oapi.api.im.v1 import *
from config import LARK_APP_ID, LARK_APP_SECRET, LARK_CHAT_ID


def get_client() -> lark.Client:
    """Create Lark API client."""
    return lark.Client.builder().app_id(LARK_APP_ID).app_secret(LARK_APP_SECRET).build()


def send_text(text: str, chat_id: str = None) -> bool:
    """Send text message to chat."""
    client = get_client()
    chat_id = chat_id or LARK_CHAT_ID
    
    req = CreateMessageRequest.builder() \
        .receive_id_type("chat_id") \
        .request_body(
            CreateMessageRequestBody.builder()
            .receive_id(chat_id)
            .msg_type("text")
            .content(json.dumps({"text": text}))
            .build()
        ).build()
    
    resp = client.im.v1.message.create(req)
    if resp.success():
        print(f"Text sent: {text[:50]}...")
        return True
    else:
        print(f"Failed: {resp.code} - {resp.msg}")
        return False


def upload_image(image_path: str) -> str:
    """Upload image and return image_key."""
    client = get_client()
    
    with open(image_path, "rb") as f:
        req = CreateImageRequest.builder() \
            .request_body(
                CreateImageRequestBody.builder()
                .image_type("message")
                .image(f)
                .build()
            ).build()
        
        resp = client.im.v1.image.create(req)
    
    if resp.success():
        image_key = resp.data.image_key
        print(f"Image uploaded: {image_key}")
        return image_key
    else:
        print(f"Upload failed: {resp.code} - {resp.msg}")
        return ""


def send_image(image_path: str, chat_id: str = None) -> bool:
    """Upload and send image to chat."""
    chat_id = chat_id or LARK_CHAT_ID
    
    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        return False
    
    image_key = upload_image(image_path)
    if not image_key:
        return False
    
    client = get_client()
    req = CreateMessageRequest.builder() \
        .receive_id_type("chat_id") \
        .request_body(
            CreateMessageRequestBody.builder()
            .receive_id(chat_id)
            .msg_type("image")
            .content(json.dumps({"image_key": image_key}))
            .build()
        ).build()
    
    resp = client.im.v1.message.create(req)
    if resp.success():
        print(f"Image sent to {chat_id}")
        return True
    else:
        print(f"Failed: {resp.code} - {resp.msg}")
        return False


def send_image_with_text(image_path: str, text: str, chat_id: str = None) -> bool:
    """Send text followed by image."""
    chat_id = chat_id or LARK_CHAT_ID
    send_text(text, chat_id)
    return send_image(image_path, chat_id)
