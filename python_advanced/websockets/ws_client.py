#!/usr/bin/env python3
"""Minimal WebSocket client."""
import asyncio

from websockets.asyncio.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to uri, send text once, receive once, return the reply."""
    async with connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
    return response


async def main():
    """Send 'Hello WebSocket' to the echo server and print the reply."""
    response = await connect_and_send("ws://127.0.0.1:8765", "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
