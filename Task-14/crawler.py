import asyncio
from collections import deque, defaultdict

from fetcher import Fetcher
from parser import extract_links
from robots_handler import RobotsHandler
from utils import normalize_url
from exporter import export_json, export_sitemap


class WebCrawler:
    def __init__(self, seed_url, max_depth, concurrency):
        self.seed_url = seed_url
        self.max_depth = max_depth
        self.concurrency = concurrency

        self.visited = set()
        self.graph = defaultdict(set)
        self.inbound_count = defaultdict(int)

        self.robots = RobotsHandler()

    async def run(self):
        queue = deque([(self.seed_url, 0)])

        async with Fetcher(self.concurrency) as fetcher:
            while queue:
                tasks = []

                for _ in range(min(len(queue), self.concurrency)):
                    url, depth = queue.popleft()

                    if depth > self.max_depth:
                        continue

                    if url in self.visited:
                        continue

                    if not self.robots.can_fetch(url):
                        continue

                    self.visited.add(url)
                    tasks.append(self.process_page(fetcher, url, depth))

                results = await asyncio.gather(*tasks)

                for links, parent, depth in results:
                    for link in links:
                        norm = normalize_url(link)

                        self.graph[parent].add(norm)
                        self.inbound_count[norm] += 1

                        if norm not in self.visited:
                            queue.append((norm, depth + 1))

        export_json(self.graph)
        export_sitemap(self.visited)

        self.print_report()

    async def process_page(self, fetcher, url, depth):
        url, status, html = await fetcher.fetch(url)

        print(f"[{status}] {url}")

        links = extract_links(url, html) if html else set()

        return links, url, depth

    def print_report(self):
        print("\n🔎 Orphan Pages:")
        for url in self.visited:
            if self.inbound_count[url] == 0 and url != self.seed_url:
                print(url)