#!/usr/bin/env python3
"""WebSocket server that broadcasts every message to all clients."""
import asyncio

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def broadcast(message):
    """Send 'B:' + message to every connected client."""
    for client in list(connected_clients):
        try:
            await client.send(f"B:{message}")
        except ConnectionClosed:
            connected_clients.discard(client)


async def connection_handler(websocket):
    """Track the client and broadcast each message it sends."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast(message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    async with serve(connection_handler, "127.0.0.1", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
