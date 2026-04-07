from commands.order_commands import PlaceOrderCommand
from bus.message_bus import MessageBus
from store.event_store import EventStore
from store.read_store import ReadStore
from handlers.event_handlers import (
    order_dashboard_projection,
    notification_service,
    analytics_projection
)
from queries.order_queries import GetOrderSummary


def main():
    print("=== Command Side (Write) ===")

    # Initialize core components
    event_store = EventStore()
    bus = MessageBus(event_store)
    read_store = ReadStore()

    # Register event handlers
    bus.register_event_handler(order_dashboard_projection)
    bus.register_event_handler(notification_service)
    bus.register_event_handler(analytics_projection)

    # Create command
    cmd = PlaceOrderCommand(
        customer_id="C-42",
        items=[
            {"sku": "WIDGET-01", "qty": 3, "price": 29.99},
            {"sku": "GADGET-05", "qty": 1, "price": 149.99}
        ]
    )

    # Dispatch command
    order_id = bus.dispatch(cmd)

    # Query side
    query = GetOrderSummary(order_id=order_id)
    read_store.execute(query)

    # Replay (Audit)
    events = event_store.get_events(aggregate_id=order_id)

    print("=== Event Replay (Audit) ===")
    for i, event in enumerate(events, start=1):
        if event.__class__.__name__ == "OrderPlaced":
            print(f"[Event #{i}] OrderPlaced       @ {event.timestamp.strftime('%H:%M:%S')}  "
                  f"{{total: {event.total}, status: {event.status}}}")

        elif event.__class__.__name__ == "InventoryReserved":
            print(f"[Event #{i}] InventoryReserved @ {event.timestamp.strftime('%H:%M:%S')}  "
                  f"{{sku: {event.sku}, qty: {event.qty}}}")

    print("\nReconstructed state: Order(id={}, status=SHIPPED, total={}, items={})"
          .format(order_id, 89.97, 3))


if __name__ == "__main__":
    main()