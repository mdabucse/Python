def add_to_cart(product_id, qty):
    if qty <= 0:
        return {"status": "error"}
    return {"status": "success", "product_id": product_id, "qty": qty}

def test_add_item_valid():
    result = add_to_cart(1, 2)
    assert result["status"] == "success"

def test_add_item_zero_qty():
    result = add_to_cart(1, 0)
    assert result["status"] == "error"

def test_add_item_large_qty():
    result = add_to_cart(2, 10)
    assert result["qty"] == 10