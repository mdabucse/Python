# Simulated Read DB (in-memory)
READ_DB = {}

# Simulated Analytics
ANALYTICS = {
    "total_revenue": 12607.36  # base value before this order
}


def order_dashboard_projection(event):
    if event.__class__.__name__ == "OrderPlaced":
        print("[HANDLER: OrderDashboardProjection] OrderPlaced -> updating read model...")

        READ_DB[event.order_id] = {
            "order_id": event.order_id,
            "customer_id": event.customer,
            "status": event.status,
            "total": event.total,
            "item_count": None,  # will fill later
            "placed_at": event.timestamp.isoformat() + "Z"
        }

        print("  Read DB: INSERT INTO order_summary (id, customer, total, status, item_count)")
        print(f"           VALUES ('{event.order_id}', '{event.customer}', {event.total}, 'PLACED', 4)\n")


def notification_service(event):
    if event.__class__.__name__ == "OrderPlaced":
        print("[HANDLER: NotificationService] OrderPlaced -> sending confirmation email...")
        print(f"  Email sent to customer {event.customer} OK\n")


def analytics_projection(event):
    if event.__class__.__name__ == "OrderPlaced":
        print("[HANDLER: AnalyticsProjection] OrderPlaced -> updating daily stats...")

        ANALYTICS["total_revenue"] += event.total

        print(f"  Today's revenue: ${ANALYTICS['total_revenue']:.2f} (+${event.total})\n")