# Real-Time Data Streaming Dashboard

A real-time dashboard that simulates sensor data, processes it using statistical techniques, and streams live updates to a browser using WebSockets.

---

##  Features

-  Simulated real-time sensor data
-  Moving Average & Z-Score calculation
-  Anomaly detection (threshold-based alerts)
-  WebSocket-based live data streaming
-  Interactive dashboard using Chart.js

---

##  Project Architecture

---

##  Project Structure

```bash
real-time-dashboard/
│
├── backend/
│   ├── main.py          # FastAPI server + WebSocket
│   ├── simulator.py     # Fake sensor data generator
│   ├── processor.py     # Data processing logic
│   └── __init__.py
│
├── frontend/
│   ├── index.html       # UI
│   ├── script.js        # WebSocket + Chart logic
└── README.md


## Output value JSON
```
{
  "value": 32.5,
  "moving_avg": 30.2,
  "z_score": 1.8,
  "alert": false
}
```