import json
import time
from config import (
    redis_client,
    QUEUE_NAME,
    DEAD_LETTER_QUEUE,
    MAX_RETRIES,
    BASE_DELAY,
    RESULT_KEY_PREFIX
)
from registry import TASK_REGISTRY
import tasks

def start_worker():
    print("Worker started...")

    while True:
        _, task_data = redis_client.blpop(QUEUE_NAME)

        task = json.loads(task_data)

        task_id = task["task_id"]
        func_name = task["function"]
        args = task["args"]
        retries = task.get("retries", 0)

        start_time = time.time()

        print(f"\n Received task: {task}")

        try:
            if func_name not in TASK_REGISTRY:
                raise Exception(f"Task '{func_name}' not found")

            func = TASK_REGISTRY[func_name]
            result = func(*args)

            duration = time.time() - start_time

            result_data = {
                "status": "SUCCESS",
                "result": result,
                "duration": duration
            }

            redis_client.set(
                f"{RESULT_KEY_PREFIX}{task_id}",
                json.dumps(result_data)
            )

            print(f" Success: {result_data}")

        except Exception as e:
            print(f" Failed: {e}")

            if retries < MAX_RETRIES:
                retries += 1
                task["retries"] = retries

                delay = BASE_DELAY * (2 ** (retries - 1))
                print(f" Retrying in {delay} sec...")

                time.sleep(delay)
                redis_client.rpush(QUEUE_NAME, json.dumps(task))

            else:
                print(" Moving to DLQ")

                duration = time.time() - start_time

                result_data = {
                    "status": "FAILED",
                    "error": str(e),
                    "duration": duration
                }

                # Store failure result
                redis_client.set(
                    f"{RESULT_KEY_PREFIX}{task_id}",
                    json.dumps(result_data)
                )

                task["error"] = str(e)
                redis_client.rpush(DEAD_LETTER_QUEUE, json.dumps(task))

if __name__ == "__main__":
    start_worker()