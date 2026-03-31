import time
from fastapi import FastAPI, Request

from utils.config import SERVICES
from utils.proxy import forward_request
from utils.rate_limiter import is_allowed
from utils.cache import get_cache, set_cache
from utils.circuit_breaker import (
    is_request_allowed,
    record_failure,
    record_success
)

app = FastAPI()

# Health stats
health_stats = {
    service: {
        "status": "UP",
        "latency": 0,
        "circuit": "CLOSED",
        "cache_hits": 0
    }
    for service in SERVICES
}


# STARTUP 

@app.on_event("startup")
async def startup():
    print("=== Gateway Startup ===")
    print("[INFO] API Gateway running on http://0.0.0.0:8080")
    print("[INFO] Routes loaded:")
    for k, v in SERVICES.items():
        print(f"       /api/{k}/**    -> {v}")


# MAIN ROUTE 

@app.api_route("/api/{service}/{path:path}", methods=["GET", "POST"])
async def gateway(service: str, path: str, request: Request):

    start_time = time.time()
    api_key = request.headers.get("x-api-key", "anonymous")
    url_key = f"{service}/{path}"

    print(f"\n[REQ] {request.method} /api/{url_key}  client={api_key}")

    # RATE LIMIT 
    allowed, count = is_allowed(api_key)
    if not allowed:
        print(f"      -> RATE LIMITED ({count}/{50} req/min) — 429 Too Many Requests")
        return {"error": "Too Many Requests"}

    # CACHE 
    if request.method == "GET":
        cached, ttl = get_cache(url_key)
        if cached:
            health_stats[service]["cache_hits"] += 1
            print(f"      -> CACHE HIT (TTL: {ttl}s remaining) — 200 OK in 2ms")
            return cached

    # CIRCUIT BREAKER 
    if not is_request_allowed(service):
        health_stats[service]["circuit"] = "OPEN"
        print(f"      -> CIRCUIT OPEN ({service}-service) — 503 Service Unavailable")
        print(f'        Fallback: {{"error": "Service temporarily unavailable", "retry_after": 30}}')
        return {
            "error": "Service temporarily unavailable",
            "retry_after": 30
        }

    # PROXY 
    try:
        body = await request.body()

        response = await forward_request(
            SERVICES[service],
            path,
            request.method,
            dict(request.headers),
            body
        )

        data = response.json()
        latency = int((time.time() - start_time) * 1000)

        # Update health
        health_stats[service]["status"] = "UP"
        health_stats[service]["latency"] = f"{latency}ms"
        health_stats[service]["circuit"] = "CLOSED"

        record_success(service)

        # Cache only GET
        if request.method == "GET":
            set_cache(url_key, data)

        print(f"      -> PROXY to {service}-service — 200 OK in {latency}ms")

        return data

    except Exception:
        record_failure(service)

        health_stats[service]["status"] = "DOWN"
        health_stats[service]["latency"] = "timeout"

        print(f"      -> ERROR contacting {service}-service")

        return {"error": "Service failed"}


# HEALTH DASHBOARD 

@app.get("/health")
async def health():
    print("\n=== Health Dashboard ===")
    print("+------------------+--------+---------+----------+-------------+")
    print("| Service          | Status | Latency | Circuit  | Cache Hits  |")
    print("+------------------+--------+---------+----------+-------------+")

    for service, stats in health_stats.items():
        print(f"| {service:<16} | {stats['status']:<6} | {stats['latency']:<7} | {stats['circuit']:<8} | {stats['cache_hits']:<11} |")

    print("+------------------+--------+---------+----------+-------------+")

    return health_stats