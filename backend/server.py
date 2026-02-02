import asyncio
import json
import datetime
import websockets

typing_data = []

async def handler(websocket):
    print("✅ Frontend connected")

    async for message in websocket:
        data = json.loads(message)

        typing_data.append(data)

        if len(typing_data) > 30:
            typing_data.pop(0)

        delays = [d["delay"] for d in typing_data]

        mean = sum(delays) / len(delays)
        variance = sum((x - mean) ** 2 for x in delays) / len(delays)
        std = variance ** 0.5

        risk_score = min(100, int((std / 100) * 50 + (20 if data["delay"] > mean else 0)))

        log = {
            "time": str(datetime.datetime.now()),
            "key": data["key"],
            "delay": data["delay"],
            "risk": risk_score
        }

        with open("keystrokes.json", "a") as f:
            f.write(json.dumps(log) + "\n")

        await websocket.send(json.dumps({
            "risk": risk_score,
            "alert": data["delay"] > mean + 2 * std
        }))

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("🚀 Server running on ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())
def on_message(data):
    print("Key received:", data)

