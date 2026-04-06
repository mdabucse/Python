# Graph Database Engine (Python)

A simple in-memory graph database built from scratch with support for nodes, edges, traversal queries, and write-ahead logging (WAL).

---

## Features

- Create **typed nodes** (Person, Company, etc.)
- Create **directed edges** with labels (FRIENDS_WITH, WORKS_AT)
- Perform **multi-hop queries**
- Compute **graph traversals**
- **Write-Ahead Logging (WAL)** for persistence
- Interactive **CLI shell**

---

## Project Structure
```
graphdb/
│
├── core/
│ ├── node.py
│ ├── edge.py
│ ├── graph.py
│
├── storage/
│ ├── wal.py
│
├── query/
│ ├── executor.py
│
├── main.py
```

## Examples
```
CREATE NODE Person name=Alice
CREATE NODE Person name=Bob
CREATE NODE Company name=AcmeCorp

CREATE EDGE 1 2 FRIENDS_WITH
CREATE EDGE 2 3 WORKS_AT

MATCH AcmeCorp
SHOW
```