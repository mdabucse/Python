import asyncio
import random

async def sensor_stream():
    while True:
        # normal temperature
        value = random.uniform(25, 35)

        # randomly create anomaly
        if random.random() < 0.1:
            value = random.uniform(70, 90)

        yield {
            "sensor_id": "sensor_1",
            "value": round(value, 2)
        }

        await asyncio.sleep(1)