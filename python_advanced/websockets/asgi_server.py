#!/usr/bin/env python3
"""ASGI application (Starlette) with an HTTP page and a WebSocket echo."""
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    """Return the HTML page."""
    return HTMLResponse("<h1>WebSocket Echo</h1>")


async def websocket_endpoint(websocket):
    """Echo every text message back to the sender."""
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
