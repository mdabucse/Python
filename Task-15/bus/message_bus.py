from aggregates.order import Order


class MessageBus:
    def __init__(self, event_store):
        self.event_store = event_store
        self.event_handlers = []

    def register_event_handler(self, handler):
        self.event_handlers.append(handler)

    def dispatch(self, command):
        # Handle PlaceOrderCommand
        if command.__class__.__name__ == "PlaceOrderCommand":
            order = Order()

            # Step 1: Aggregate creates events
            events = order.place_order(
                customer_id=command.customer_id,
                items=command.items
            )

            # Step 2: Store events
            self.event_store.append(order.id, events)

            # Step 3: Publish events
            self.publish(events)

            return order.id

    def publish(self, events):
        print(f"[BUS] Published {len(events)} events to \"orders\" topic\n")

        for event in events:
            for handler in self.event_handlers:
                handler(event)