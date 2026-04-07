import aiohttp
import asyncio

class Fetcher:
    def __init__(self, concurrency):
        self.session = None
        self.semaphore = asyncio.Semaphore(concurrency)

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *args):
        await self.session.close()

    async def fetch(self, url):
        async with self.semaphore:
            try:
                async with self.session.get(url, timeout=10) as response:
                    return url, response.status, await response.text()
            except Exception:
                return url, None, ""