
# CantinaCoin Blockchain

CantinaCoin is a simple decentralized cryptocurrency powered by a blockchain. This project demonstrates the basic principles of a blockchain such as transactions, mining, proof of work, and consensus algorithms. It uses Python for the backend and FastAPI for providing a REST API to interact with the blockchain.
![CantinaCoin Icon](image.png)
## Features

- **Transaction Creation**: Users can create transactions that will be included in the blockchain.
- **Mining**: Mine new blocks with proof of work and add them to the blockchain.
- **Blockchain Validation**: Ensure the integrity of the blockchain with validation mechanisms.
- **Node Registration**: Register new nodes to the network, supporting a decentralized architecture.
- **Conflict Resolution**: Resolve conflicts between nodes using the longest valid chain rule.
- **Persistent Storage**: Save the blockchain to a local JSON file for persistence across restarts.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Proof of Work](#proof-of-work)
- [Consensus Algorithm](#consensus-algorithm)
- [Running Multiple Nodes](#running-multiple-nodes)
- [License](#license)

---

## Getting Started

### Prerequisites

Ensure you have Python 3.7+ installed. You will also need `pip` to install the dependencies.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cantinacoin.git
cd cantinacoin
```

### 2. Create a Virtual Environment

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scriptsctivate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Server

Start the FastAPI server with Uvicorn:

```bash
uvicorn api:app --reload --port 8000
```

Your API will be running at `http://127.0.0.1:8000`.

You can interact with the API through Swagger UI at:
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## API Endpoints

### 1. **Get the Blockchain**

`GET /chain`

Fetch the full blockchain.

**Response:**
```json
{
  "length": 1,
  "chain": [
    {
      "index": 1,
      "timestamp": 1714416761.874,
      "transactions": [],
      "proof": 100,
      "previous_hash": "1"
    }
  ]
}
```

### 2. **Create a New Transaction**

`POST /transactions/new`

Create a new transaction. The transaction will be added to the next block.

**Request Body:**
```json
{
  "sender": "Alice",
  "recipient": "Bob",
  "amount": 50.0
}
```

**Response:**
```json
{
  "message": "Transaction will be added to block 2"
}
```

### 3. **Mine a New Block**

`GET /mine`

Mine a new block and add it to the blockchain.

**Response:**
```json
{
  "message": "New Block Forged",
  "block": {
    "index": 2,
    "timestamp": 1714416762.874,
    "transactions": [
      {
        "sender": "Alice",
        "recipient": "Bob",
        "amount": 50.0
      }
    ],
    "proof": 832947,
    "previous_hash": "abc123"
  }
}
```

### 4. **Check Blockchain Validity**

`GET /valid`

Check if the blockchain is valid (i.e., all blocks are properly linked and proof of work is correct).

**Response:**
```json
{
  "is_valid": true
}
```

### 5. **Register New Nodes**

`POST /nodes/register`

Register new nodes to the network.

**Request Body:**
```json
{
  "nodes": ["http://127.0.0.1:8001"]
}
```

**Response:**
```json
{
  "message": "Nodes registered",
  "total_nodes": ["http://127.0.0.1:8001"]
}
```

### 6. **Resolve Conflicts**

`GET /nodes/resolve`

Resolve conflicts with other nodes by syncing with the longest valid chain.

**Response:**
```json
{
  "message": "Our chain was replaced",
  "new_chain": [
    {
      "index": 1,
      "timestamp": 1714416761.874,
      "transactions": [],
      "proof": 100,
      "previous_hash": "1"
    },
    {
      "index": 2,
      "timestamp": 1714416762.874,
      "transactions": [
        {
          "sender": "Alice",
          "recipient": "Bob",
          "amount": 50.0
        }
      ],
      "proof": 832947,
      "previous_hash": "abc123"
    }
  ]
}
```

---

## Proof of Work

The Proof of Work (PoW) algorithm is a mechanism that ensures the blockchain is secure and tamper-proof. The algorithm requires miners to solve a computational puzzle, where the hash of the combined `last_proof` and `current_proof` must start with a certain number of leading zeros.
