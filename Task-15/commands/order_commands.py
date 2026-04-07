class PlaceOrderCommand:
    def __init__(self, customer_id: str, items: list):
        self.customer_id = customer_id
        self.items = items