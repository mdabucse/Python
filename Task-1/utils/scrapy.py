from .parser import parse_product
from .config import BASE_URL, TOTAL_PAGES
from .logger import log

log("Scraper started — target: Snapdeal")

async def scrape(page):
    all_data = []

    for page_num in range(1, TOTAL_PAGES + 1):
        print(f"\nScraping Page {page_num}...")
        

        url = BASE_URL.format(page_num)
        await page.goto(url)

        await page.wait_for_selector(".product-tuple-listing")

        products = await page.query_selector_all(".product-tuple-listing")
        for product in products:
            data = await parse_product(product)
            all_data.append(data)
        log(f"Page {page_num}/{TOTAL_PAGES} — {len(products)} products extracted")
        

    return all_data