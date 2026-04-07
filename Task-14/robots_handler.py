from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

class RobotsHandler:
    def __init__(self):
        self.parsers = {}

    def can_fetch(self, url):
        domain = urlparse(url).netloc

        if domain not in self.parsers:
            rp = RobotFileParser()
            rp.set_url(f"https://{domain}/robots.txt")
            rp.read()
            self.parsers[domain] = rp

        return self.parsers[domain].can_fetch("*", url)