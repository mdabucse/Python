from fastapi import FastAPI, WebSocket
from simulator import sensor_stream
from processor import Processor

app = FastAPI()
processor = Processor()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    async for data in sensor_stream():
        result = processor.process(data["value"])

        await websocket.send_json(result)