# Concurrent Web Crawler with Depth Control

## Overview

A high-performance asynchronous web crawler that starts from a seed URL and explores links level-by-level (BFS) up to a specified depth. It supports concurrency, deduplication, robots.txt compliance, and exports results as JSON and XML.

---

##  Features

* Asynchronous crawling using `asyncio` and `aiohttp`
* Depth-controlled BFS traversal
* Deduplication (avoids revisiting URLs)
* `robots.txt` compliance
* Status tracking (200, 404, 301/302)
* Orphan page detection (no inbound links)
* Export:

  * Crawl graph → `JSON`
  * Sitemap → `XML`

---

## Project Structure

```
crawler/
│
├── main.py
├── crawler.py
├── fetcher.py
├── parser.py
├── robots_handler.py
├── utils.py
├── exporter.py
│
├── data/
│   ├── graph.json
│   └── sitemap.xml
│
└── requirements.txt
```

---

## Installation

```bash
uv add aiohttp beautifulsoup4
```

---

##  Usage

```bash
python main.py --url https://example.com --depth 2 --concurrency 5
```

### Arguments

* `--url` → Starting URL (seed)
* `--depth` → Max crawl depth (default: 2)
* `--concurrency` → Number of parallel requests (default: 5)

---

## How It Works

1. Start from the seed URL
2. Crawl pages level-by-level (BFS)
3. Extract links from each page
4. Skip:

   * Already visited URLs
   * Disallowed URLs (robots.txt)
5. Track:

   * Link relationships (graph)
   * Inbound link counts
6. Export results

---

##  Output

###  JSON Graph (`data/graph.json`)

* Shows page-to-page link relationships

###  XML Sitemap (`data/sitemap.xml`)

* List of all discovered URLs

---

##  Additional Insights

* Detects broken links (404)
* Identifies redirects (301/302)
* Finds orphan pages (no inbound links)


## Summary

A scalable and efficient web crawler that mimics how search engines explore websites — fast, structured, and rule-compliant.

---
