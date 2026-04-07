import uuid
from events.order_events import OrderPlaced, InventoryReserved


class Order:
    def __init__(self):
        self.id = None
        self.customer_id = None
        self.items = []
        self.total = 0.0
        self.events = []

    def place_order(self, customer_id: str, items: list):
        print("[WRITE] PlaceOrderCommand received")

        # Generate Order ID
        self.id = f"ORD-{str(uuid.uuid4())[:4]}"
        self.customer_id = customer_id
        self.items = items

        print(f"[WRITE] Aggregate Order#{self.id} created")

        # Calculate total
        total = 0.0
        for item in items:
            total += item["qty"] * item["price"]

        self.total = round(total, 2)

        # Create OrderPlaced event
        order_event = OrderPlaced(
            order_id=self.id,
            customer=customer_id,
            total=self.total
        )

        self.events.append(order_event)

        # Create InventoryReserved events
        for item in items:
            inv_event = InventoryReserved(
                sku=item["sku"],
                qty=item["qty"]
            )
            self.events.append(inv_event)

        return self.events