SERVICES = {
    "users": "http://localhost:3001",
    "orders": "http://localhost:3002",
    "products": "http://localhost:3003",
}

RATE_LIMIT = 50        # requests per minute per API key
CACHE_TTL = 60        # seconds
CIRCUIT_FAIL_THRESHOLD = 5
CIRCUIT_RESET_TIMEOUT = 30  # seconds