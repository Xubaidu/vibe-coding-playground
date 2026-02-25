"""Lark Event Subscription via WebSocket (长连接)."""

import lark_oapi as lark
from lark_oapi.api.im.v1 import *
from config import LARK_APP_ID, LARK_APP_SECRET


def handle_message_receive(data: P2ImMessageReceiveV1) -> None:
    """Handle received messages."""
    msg = data.event.message
    print(f"[Message Received]")
    print(f"  Chat ID: {msg.chat_id}")
    print(f"  Content: {msg.content}")
    print()


def start_event_subscription():
    """Start WebSocket connection to receive events."""
    
    if not LARK_APP_ID or not LARK_APP_SECRET:
        print("Error: LARK_APP_ID and LARK_APP_SECRET required in config")
        return
    
    event_handler = (
        lark.EventDispatcherHandler.builder("", "")
        .register_p2_im_message_receive_v1(handle_message_receive)
        .build()
    )
    
    cli = lark.ws.Client(
        app_id=LARK_APP_ID,
        app_secret=LARK_APP_SECRET,
        event_handler=event_handler,
        log_level=lark.LogLevel.DEBUG
    )
    
    print("Starting Lark WebSocket connection...")
    print("Listening for events. Press Ctrl+C to stop.")
    cli.start()


if __name__ == "__main__":
    start_event_subscription()
