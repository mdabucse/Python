# Blockchain Prototype

## Overview

A simplified blockchain system with:

* Proof-of-Work mining
* Transaction signing
* Merkle tree validation
* Modular architecture

---

## Key Components

* **Block** → Stores transactions + hash
* **Blockchain** → Manages chain & mining
* **Transaction** → Structured & validated data
* **Wallet** → Key generation & signing
* **Utils** → Verification + Merkle root

---

## Project Structure

```
blockchain_project/
│
├── block.py
├── blockchain.py
├── transaction.py
├── wallet.py
├── utils.py
└── main.py
```

---

## Core Flow

```
Wallet → Sign → Transaction
        ↓
Mempool → Mining
        ↓
Block Created → Proof of Work
        ↓
Added to Chain → Verified
```

---

## Key Features

* Secure transactions (signature-based)
* Tamper-proof blocks (Merkle root)
* Mining with difficulty
* Modular & extendable design

---

## Outcome

A working mini-blockchain system ready for:

* P2P networking
* API integration
* Hackathon projects 
