"""Query Lark chat/group IDs by name."""

import sys
sys.path.insert(0, str(__file__).rsplit("/", 2)[0])  # Add parent to path

import lark_oapi as lark
from lark_oapi.api.im.v1 import *
from config import LARK_APP_ID, LARK_APP_SECRET


def get_client() -> lark.Client:
    return lark.Client.builder().app_id(LARK_APP_ID).app_secret(LARK_APP_SECRET).build()


def search_chats(keyword: str = "") -> list:
    """Search for chats by keyword."""
    client = get_client()
    req = SearchChatRequest.builder().page_size(50).query(keyword).build()
    resp = client.im.v1.chat.search(req)
    
    if resp.success() and resp.data and resp.data.items:
        return [(c.chat_id, c.name) for c in resp.data.items]
    return []


def list_bot_chats() -> list:
    """List all chats the bot is in."""
    client = get_client()
    req = ListChatRequest.builder().page_size(50).build()
    resp = client.im.v1.chat.list(req)
    
    if resp.success() and resp.data and resp.data.items:
        return [(c.chat_id, c.name) for c in resp.data.items]
    return []


if __name__ == "__main__":
    if len(sys.argv) > 1:
        results = search_chats(sys.argv[1])
    else:
        results = list_bot_chats()
    
    for chat_id, name in results:
        print(f"{chat_id}  {name}")
