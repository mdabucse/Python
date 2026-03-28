from fastapi import FastAPI, WebSocket
import json
from database import save_message, get_messages

app = FastAPI()

# room_name  list of connections
rooms = {}

# websocket  user info
user_info = {}

# username  websocket
active_users = {}


#  Send updated user list to room
async def broadcast_users(room):
    users = [
        user_info[ws]["username"]
        for ws in rooms.get(room, [])
    ]

    data = {
        "type": "users",
        "users": users
    }

    for conn in rooms.get(room, []):
        await conn.send_text(json.dumps(data))


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()

    # receive username & room
    username = await ws.receive_text()
    room = await ws.receive_text()

    # store user
    user_info[ws] = {"username": username, "room": room}
    active_users[username] = ws

    # create room if not exists
    if room not in rooms:
        rooms[room] = []

    rooms[room].append(ws)

    print(f"{username} joined {room}")

    #  LOAD OLD MESSAGES FROM MYSQL
    old_messages = get_messages(room)
    for msg_id, user, msg in old_messages:
        await ws.send_text(json.dumps({
            "type": "room",
            "user": user,
            "message": msg
        }))

    # broadcast updated users
    await broadcast_users(room)

    # notify join
    for conn in rooms[room]:
        await conn.send_text(json.dumps({
            "type": "status",
            "message": f"{username} joined"
        }))

    try:
        while True:
            data = json.loads(await ws.receive_text())

            # TYPING INDICATOR
            if data.get("type") == "typing":
                for conn in rooms[room]:
                    if conn != ws:
                        await conn.send_text(json.dumps({
                            "type": "typing",
                            "user": username,
                            "status": data["status"]
                        }))
                continue

            message = data.get("message")
            target = data.get("to")

            # SAVE ROOM MESSAGE TO MYSQL
            if not target and message:
                save_message(room, username, message)

            # PRIVATE MESSAGE
            if target:
                if target in active_users:
                    target_ws = active_users[target]

                    await target_ws.send_text(json.dumps({
                        "type": "private",
                        "from": username,
                        "message": message
                    }))
                else:
                    await ws.send_text(json.dumps({
                        "type": "error",
                        "message": "User not found"
                    }))

            # ROOM MESSAGE
            else:
                for conn in rooms[room]:
                    await conn.send_text(json.dumps({
                        "type": "room",
                        "user": username,
                        "message": message
                    }))

    except:
        print(f"{username} disconnected")

        # remove user
        rooms[room].remove(ws)
        del user_info[ws]
        del active_users[username]

        # notify leave
        for conn in rooms.get(room, []):
            await conn.send_text(json.dumps({
                "type": "status",
                "message": f"{username} left"
            }))

        # update user list
        if room in rooms:
            await broadcast_users(room)

        # remove empty room
        if room in rooms and len(rooms[room]) == 0:
            del rooms[room]