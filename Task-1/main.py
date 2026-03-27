import asyncio
from playwright.async_api import async_playwright
from utils.scrapy import scrape
from utils.storage import save_to_csv
from utils.database import insert_products,get_previous_prices
from utils.report import compare_prices,print_report

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        old_data = get_previous_prices()
        new_data = await scrape(page)

        await browser.close()
        changes = compare_prices(old_data,new_data)
        insert_products(new_data)
        print_report(changes)
        save_to_csv(changes)


asyncio.run(main())