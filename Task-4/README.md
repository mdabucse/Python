# Distributed Task Queue System (Mini Celery Clone)

A lightweight distributed task queue built using **Python + Redis**, inspired by systems like Celery.  
This project demonstrates **asynchronous task processing, retries, fault tolerance, and monitoring**.

---

## Features

- Producer-Consumer architecture
- Redis-based task queue (message broker)
- Dynamic task execution (function registry)
- Retry mechanism with exponential backoff
- Dead Letter Queue (DLQ) for failed tasks
- Result backend (task status + output storage)
- CLI + Web dashboard for monitoring
- Simulated multi-worker processing

---

## Architecture
```
Producer → Redis Queue → Worker(s) → Result Backend
↓
Dead Letter Queue
↓
Dashboard / CLI
```

## Project Structure
```
├── config.py # Redis config + constants
├── producer.py # Task producer
├── worker.py # Worker (consumer)
├── tasks.py # Task definitions
├── registry.py # Task registry (decorator)
├── get_result.py # Fetch task result
├── dashboard.py # Flask dashboard
├── dashboard_cli.py # CLI dashboard
└── README.md
```

## Output
```
+----------+--------+-------------+--------+-------------+
| Task ID  | Func   | Status      | Retries| Duration    |
+----------+--------+-------------+--------+-------------+
| a8f3c1   | thumb  | SUCCESS     | 0      | 1.34s       |
| b7d4e2   | email  | SUCCESS     | 2      | 6.82s       |
| c9e5f3   | report | DEAD_LETTER | 3      | —           |
+----------+--------+-------------+--------+-------------+
```