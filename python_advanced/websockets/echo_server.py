#!/usr/bin/env python3
"""Minimal WebSocket echo server."""
import asyncio

from websockets.asyncio.server import serve


async def connection_handler(websocket):
    """Echo every text message back to the sender."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
