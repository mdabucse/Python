# Real-Time Chat Application with WebSockets

A real-time multi-room chat application built with FastAPI and WebSockets, featuring instant messaging, private chats, typing indicators, and user presence tracking with MySQL persistence.

---

## Overview

This project demonstrates a production-grade real-time communication system that supports multiple concurrent users across different chat rooms. The application uses WebSocket technology for bidirectional communication and MySQL for persistent storage of messages and chat history.

---

## Features

### Real-Time Communication
- **WebSocket-based bidirectional communication** — Instant message delivery without requiring page refreshes
- **Low-latency message propagation** — Messages delivered to all connected clients in milliseconds

### Chat Functionality
- **Multi-room support** — Create and join multiple isolated chat rooms simultaneously
- **Private messaging** — Direct one-to-one conversations between users
- **Broadcast messaging** — Send messages to all users within a room
- **Chat history** — Message persistence and automatic history loading upon joining

### User Presence & Status
- **Real-time user list** — See who's currently online in each room
- **Join/leave notifications** — Automatic notifications when users enter or leave rooms
- **Online status tracking** — Track user availability across rooms

### Enhanced User Experience
- **Typing indicators** — See when other users are composing messages
- **Dynamic user selection** — Click to switch between room chat and private conversations
- **Responsive interface** — Works seamlessly on desktop and mobile browsers

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | FastAPI, WebSockets, Python 3.8+ |
| **Database** | MySQL 5.7+ |
| **Frontend** | HTML5, Vanilla JavaScript |
| **Protocol** | WebSocket (WSS for production) |

---

## Project Structure

```
chat-app/
├── main.py              # FastAPI WebSocket server & routing
├── db_mysql.py          # MySQL connection & CRUD operations
├── index.html           # Frontend user interface
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
```

### File Responsibilities

**main.py**
- WebSocket connection handling
- Room and user management
- Message routing (room broadcast & private)
- Typing indicator state management
- User presence tracking
- MySQL database integration

**database.py**
- MySQL connection pooling
- Message insertion & retrieval
- Chat history queries
- Database error handling

**index.html**
- Responsive user interface
- WebSocket client implementation
- Real-time DOM updates
- User interaction handlers

---

## Database Schema

### Messages Table

```sql
CREATE TABLE messages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  room VARCHAR(255) NOT NULL,
  username VARCHAR(255) NOT NULL,
  message TEXT NOT NULL,
);
```

---

## WebSocket Protocol

### Connection Flow

```
1. Client initiates WebSocket connection to /ws
   ↓
2. Client sends join message with username & room
   ↓
3. Server registers user in room
   ↓
4. Server sends chat history to connecting user
   ↓
5. Server broadcasts join notification to room
   ↓
6. Bidirectional messaging begins
```

### Message Types

**Join Event**
```json
{
  "type": "join",
  "username": "john_doe",
  "room": "general"
}
```

**Room Message**
```json
{
  "type": "message",
  "username": "john_doe",
  "room": "general",
  "content": "Hello everyone!"
}
```

**Private Message**
```json
{
  "type": "private",
  "username": "john_doe",
  "to_user": "jane_doe",
  "content": "Hi Jane!"
}
```

**Typing Indicator**
```json
{
  "type": "typing",
  "username": "john_doe",
  "room": "general"
}
```

**Leave Event**
```json
{
  "type": "leave",
  "username": "john_doe",
  "room": "general"
}
```

---

## API Endpoints

### WebSocket Endpoint

**`GET /ws`**

Establishes WebSocket connection for real-time communication.

- **Connection URL:** `ws://localhost:8000/ws`
- **Headers:** None required (no authentication currently)
- **Response:** Immediate confirmation + chat history
