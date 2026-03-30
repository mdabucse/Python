import json
import uuid
from config import redis_client, QUEUE_NAME

def send_task(function_name, args):
    task_id = str(uuid.uuid4())

    task = {
        "task_id": task_id,
        "function": function_name,
        "args": args,
        "retries": 0
    }

    redis_client.rpush(QUEUE_NAME, json.dumps(task))

    print(f" Task sent: {task}")
    return task_id


if __name__ == "__main__":
    send_task("add", [2, 3])
    send_task("multiply", [4, 5])