#!/usr/bin/env python3
"""WebSocket server with connection tracking and unicast replies."""
import asyncio

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Track the client and reply only to it with 'U:' + message."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    async with serve(connection_handler, "127.0.0.1", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
