import redis

# Redis connection
redis_client = redis.Redis(
    host="localhost",   # Redis runs via Docker on your machine
    port=6379,
    db=0,
    decode_responses=True  # ensures strings instead of bytes
)

# Main task queue
QUEUE_NAME = "task_queue"


# Dead Letter Queue (for failed tasks)
DEAD_LETTER_QUEUE = "dead_letter_queue"

# Result storage key prefix
RESULT_KEY_PREFIX = "task_result:"

# Retry settings
MAX_RETRIES = 3
BASE_DELAY = 1  # seconds (used for exponential backoff later)