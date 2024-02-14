import asyncio
from websockets.server import serve
import json

async def echo(websocket, path):
    async for message in websocket:
        jsonData = json.loads(message)
        print(jsonData)
        await websocket.send('ji')

async def main():
    async with serve(echo, "localhost", 8765):
        print("Server listening on port 8765...")
        await asyncio.Future()  # run forever

asyncio.run(main())