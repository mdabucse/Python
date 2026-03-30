from flask import Flask, jsonify
import json
from config import redis_client, RESULT_KEY_PREFIX, DEAD_LETTER_QUEUE

app = Flask(__name__)

@app.route("/")
def home():
    return " Task Queue Dashboard Running"


@app.route("/tasks")
def get_tasks():
    keys = redis_client.keys(f"{RESULT_KEY_PREFIX}*")

    results = []

    for key in keys:
        data = redis_client.get(key)
        if data:
            results.append({
                "task_id": key.replace(RESULT_KEY_PREFIX, ""),
                **json.loads(data)
            })

    return jsonify(results)


@app.route("/failed")
def failed_tasks():
    tasks = redis_client.lrange(DEAD_LETTER_QUEUE, 0, -1)

    return jsonify([json.loads(t) for t in tasks])


if __name__ == "__main__":
    app.run(debug=True)