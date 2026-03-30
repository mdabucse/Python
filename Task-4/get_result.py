import json
from config import redis_client, RESULT_KEY_PREFIX

def get_result(task_id):
    data = redis_client.get(f"{RESULT_KEY_PREFIX}{task_id}")

    if not data:
        return "Task not completed yet"

    return json.loads(data)


if __name__ == "__main__":
    task_id = input("Enter task_id: ")
    print(get_result(task_id))