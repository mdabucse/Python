from datetime import datetime


class BaseEvent:
    def __init__(self):
        self.timestamp = datetime.utcnow()


class OrderPlaced(BaseEvent):
    def __init__(self, order_id: str, customer: str, total: float):
        super().__init__()
        self.order_id = order_id
        self.customer = customer
        self.total = total
        self.status = "PLACED"


class InventoryReserved(BaseEvent):
    def __init__(self, sku: str, qty: int):
        super().__init__()
        self.sku = sku
        self.qty = qty