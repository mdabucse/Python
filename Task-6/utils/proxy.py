import httpx

async def forward_request(
    service_url: str,
    path: str,
    method: str,
    headers: dict,
    body: bytes
):
    async with httpx.AsyncClient() as client:
        url = f"{service_url}/{path}"

        response = await client.request(
            method=method,
            url=url,
            headers=headers,
            content=body
        )

        return response