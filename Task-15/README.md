# Event-Driven Microservice with CQRS Pattern

##  Overview

This project demonstrates a **complete implementation** of:

* **CQRS (Command Query Responsibility Segregation)**
* **Event Sourcing**
* **Event-Driven Architecture**

It separates **write operations (commands)** from **read operations (queries)** and stores all system changes as **events**.

---

##  Architecture Flow

```
Command → Aggregate → Events → Event Store → Message Bus → Event Handlers → Read Store → Query
```

---

##  Project Structure

```
event_cqrs/
│
├── main.py
├── commands/
│   └── order_commands.py
├── events/
│   └── order_events.py
├── aggregates/
│   └── order.py
├── bus/
│   └── message_bus.py
├── store/
│   ├── event_store.py
│   └── read_store.py
├── handlers/
│   └── event_handlers.py
└── queries/
    └── order_queries.py
```

---

##  How It Works

###  Command Side (Write)

* A command (`PlaceOrderCommand`) is created
* Sent to the **Message Bus**
* Processed by the **Order Aggregate**

###  Event Creation

The aggregate generates events:

* `OrderPlaced`
* `InventoryReserved`

###  Event Store

* Stores all events in **append-only format**
* Acts as the **single source of truth**

###  Event Handlers (Async Simulation)

Each event triggers multiple handlers:

*  Dashboard Projection → updates read model
*  Notification Service → sends email
*  Analytics Projection → updates revenue

###  Query Side (Read)

* Reads from **denormalized read store**
* Provides **fast response (~1ms)**

###  Event Replay (Audit)

* Rebuild system state using event history
* Useful for debugging and auditing

---

##  Execution Flow Example

```
=== Command Side (Write) ===
[WRITE] PlaceOrderCommand received
[WRITE] Aggregate Order#ORD-1087 created

[EVENT STORE] Appended events:
  1. OrderPlaced
  2. InventoryReserved
  3. InventoryReserved

[BUS] Published 3 events to "orders" topic

=== Event Handlers ===
[HANDLER: OrderDashboardProjection] Updating read model
[HANDLER: NotificationService] Sending email
[HANDLER: AnalyticsProjection] Updating revenue

=== Query Side (Read) ===
Order fetched in ~1ms

=== Event Replay (Audit) ===
Events replayed successfully
```

---

## Core Concepts

### ✔ CQRS

* **Write Side:** Commands + Aggregates
* **Read Side:** Queries + Read Store

### ✔ Event Sourcing

* Store **events instead of current state**
* Enables:

  * Replay 
  * Audit 
  * Debugging 

### ✔ Pub/Sub Model

* Events are published
* Multiple handlers react independently

---
