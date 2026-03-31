# app/routes.py

from fastapi import APIRouter, Request
from utils.config import SERVICES
from utils.proxy import forward_request

router = APIRouter()

@router.api_route(
    "/api/{service}/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE"]
)
async def gateway(service: str, path: str, request: Request):

    # 1. Check service exists
    if service not in SERVICES:
        return {"error": "Service not found"}

    # 2. Extract request data
    body = await request.body()
    headers = dict(request.headers)
    method = request.method

    # 3. Forward request
    response = await forward_request(
        service_url=SERVICES[service],
        path=path,
        method=method,
        headers=headers,
        body=body
    )

    # 4. Return response
    return response.json()