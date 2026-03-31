#  Async API Gateway with Rate Limiting, Caching & Circuit Breaker

A production-style **API Gateway** built using **FastAPI** that acts as a reverse proxy for multiple microservices with advanced features like:

* Rate Limiting (per API key)
* Response Caching (TTL-based)
* Circuit Breaker (failure protection)
* Health Dashboard
* Dynamic Routing to services

---

## Architecture Overview

```
Client
  ↓
API Gateway (FastAPI)
  ↓
[ Middleware Layer ]
  ├── Rate Limiter 
  ├── Cache 
  ├── Circuit Breaker 
  ↓
Proxy Layer 
  ↓
Microservices (Users, Orders, Products)
```

---

##  Project Structure

```
Task-6/
│
├── main.py
├── utils/
│   ├── config.py
│   ├── proxy.py
│   ├── rate_limiter.py
│   ├── cache.py
│   ├── circuit_breaker.py
│   ├── routes.py
│
├── case/
│   ├── users.py
│   ├── orders.py
│   ├── products.py
```

---

## Features

### Rate Limiting

* Limits requests per API key
* Example: **50 requests/minute**
* Prevents abuse & overload

---

### Caching

* Caches GET responses
* TTL-based (default: 60 seconds)
* Improves performance & reduces backend load

---

### Circuit Breaker

* Opens after **5 consecutive failures**
* Stops hitting failed service
* Auto-resets after timeout (30s)

---

### Reverse Proxy Routing

| Endpoint           | Service         |
| ------------------ | --------------- |
| `/api/users/**`    | user-service    |
| `/api/orders/**`   | order-service   |
| `/api/products/**` | product-service |

---

### Health Dashboard

```
GET /health
```

Displays:

* Service status
* Latency
* Circuit state
* Cache hits

---

##  Getting Started

---

###  Install Dependencies

```
uv add fastapi uvicorn httpx
```

---

###  Run Microservices

Open **3 terminals**

####  Users Service

```
uv run uvicorn users:app --port 3001
```

####  Orders Service

```
uv run uvicorn orders:app --port 3002
```

#### Products Service

```
uv run uvicorn products:app --port 3003
```

---

###  Run API Gateway

```
uv run uvicorn main:app --port 8080 --reload
```

---

##  Usage Examples

---

###  Call via Gateway

#### Products

```
GET http://localhost:8080/api/products/42
```

#### Users

```
GET http://localhost:8080/api/users/profile
```

#### Orders

```
GET http://localhost:8080/api/orders/latest
```
