class EventStore:
    def __init__(self):
        # {aggregate_id: [events]}
        self.store = {}

    def append(self, aggregate_id: str, events: list):
        if aggregate_id not in self.store:
            self.store[aggregate_id] = []

        print("[EVENT STORE] Appended events:")

        for i, event in enumerate(events, start=1):
            self.store[aggregate_id].append(event)

            # Pretty print based on event type
            if event.__class__.__name__ == "OrderPlaced":
                print(f"  {i}. OrderPlaced       "
                      f"{{order_id: \"{event.order_id}\", "
                      f"customer: \"{event.customer}\", "
                      f"total: ${event.total}}}")

            elif event.__class__.__name__ == "InventoryReserved":
                print(f"  {i}. InventoryReserved "
                      f"{{sku: \"{event.sku}\", qty: {event.qty}}}")

    def get_events(self, aggregate_id: str):
        return self.store.get(aggregate_id, [])

    def replay(self, aggregate_id: str):
        events = self.get_events(aggregate_id)

        print(f"\n=== Event Replay (Audit) ===")
        for i, event in enumerate(events, start=1):
            print(f"[Event #{i}] {event.__class__.__name__} "
                  f"@ {event.timestamp.strftime('%H:%M:%S')}")

        return events

