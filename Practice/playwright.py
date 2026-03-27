from playwright.sync_api import sync_playwright

def scrape_snapdeal():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.snapdeal.com/search?keyword=laptop")

        page.wait_for_selector(".product-title")

        products = page.query_selector_all(".product-title")

        for p in products[:5]:
            print(p.inner_text())
            
        browser.close()

scrape_snapdeal()