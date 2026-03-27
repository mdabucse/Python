async def parse_product(product):

    def clean_price(price_text):
        price = price_text.replace("Rs.", "").replace(",", "").strip()
        return float(price)
    
    title_el = await product.query_selector(".product-title")
    title = await title_el.inner_text() if title_el else "No Title"

    price_el = await product.query_selector(".product-price")
    price = await price_el.inner_text() if price_el else "No Price"

    return {
        "title": title,
        "price": clean_price(price)
    }