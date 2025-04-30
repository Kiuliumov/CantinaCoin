
# 🌟 CantinaCoin Blockchain

CantinaCoin is a decentralized cryptocurrency powered by a custom blockchain, built using Python and FastAPI. This project demonstrates blockchain fundamentals like transactions, mining, proof of work, consensus algorithms, and node registration. It is designed for learning, exploration, and building on top of it.

![CantinaCoin Icon](image.png)

---

## 🚀 Features

- **Transaction Creation**: Create transactions that get included in new blocks.
- **Mining**: Mine new blocks using Proof of Work.
- **Blockchain Validation**: Ensure the integrity of the blockchain using built-in validation.
- **Node Registration**: Add new nodes to the network for a decentralized system.
- **Conflict Resolution**: Automatically resolve conflicts by syncing with the longest valid chain.
- **Persistent Storage**: Store the blockchain in a JSON file for persistence.

---

## 📦 Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Proof of Work](#proof-of-work)
- [Consensus Algorithm](#consensus-algorithm)
- [Running Multiple Nodes](#running-multiple-nodes)
- [License](#license)

---

## 🏁 Getting Started

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

## 🌍 API Endpoints

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

---

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

---

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

---

### 4. **Check Blockchain Validity**

`GET /valid`

Check if the blockchain is valid (i.e., all blocks are properly linked and proof of work is correct).

**Response:**

```json
{
  "is_valid": true
}
```

---

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

---

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

## 💡 Proof of Work

The **Proof of Work** algorithm is a mechanism that ensures the blockchain is secure and tamper-proof. The algorithm requires miners to solve a computational puzzle, where the hash of the combined `last_proof` and `current_proof` must start with a certain number of leading zeros.

---

## 🤝 Consensus Algorithm

To maintain the integrity of the decentralized network, **CantinaCoin** implements a consensus algorithm based on the **longest valid chain rule**. This algorithm ensures that nodes in the network work together to agree on the single valid blockchain. If a node discovers a longer and valid chain from another node, it will adopt that chain and replace its own.

---

## 🖧 Running Multiple Nodes

To run a multi-node blockchain network:

1. **Start one instance of the CantinaCoin API** as the main node:

```bash
uvicorn api:app --reload --port 8000
```

2. **Start other nodes** on different ports (e.g., 8001, 8002):

```bash
uvicorn api:app --reload --port 8001
```

3. **Register the new nodes** in the main node by calling the `/nodes/register` endpoint.

4. **Resolve conflicts** to sync the blockchain across all nodes by calling the `/nodes/resolve` endpoint.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
