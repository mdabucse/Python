import time
from collections import defaultdict, deque
from utils.config import RATE_LIMIT
request_store = defaultdict(deque)


def is_allowed(api_key: str):
    current_time = time.time()
    window = 60  # 1 minute window

    queue = request_store[api_key]

    # Remove old requests (outside 1 min window)
    while queue and current_time - queue[0] > window:
        queue.popleft()

    # Check limit
    if len(queue) >= RATE_LIMIT:
        return False, len(queue)

    # Add current request
    queue.append(current_time)

    return True, len(queue)