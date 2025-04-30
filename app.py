from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from chain.chain import Blockchain

app = FastAPI(title="CantinaCoin API")
blockchain = Blockchain()

class TransactionRequest(BaseModel):
    sender: str
    recipient: str
    amount: float

class NodeList(BaseModel):
    nodes: List[str]

@app.get("/chain")
def get_chain():
    return {
        "length": len(blockchain.chain),
        "chain": [block.to_dict() for block in blockchain.chain]
    }

@app.post("/transactions/new")
def create_transaction(tx: TransactionRequest):
    index = blockchain.new_transaction(tx.sender, tx.recipient, tx.amount)
    return {"message": f"Transaction will be added to block {index}"}

@app.get("/mine")
def mine_block():
    block = blockchain.mine_block()
    return {"message": "New Block Forged", "block": block.to_dict()}

@app.get("/valid")
def check_validity():
    valid = blockchain.is_chain_valid()
    return {"is_valid": valid}

@app.post("/nodes/register")
def register_nodes(payload: NodeList):
    for node in payload.nodes:
        try:
            blockchain.register_node(node)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid node address: {node}")
    return {"message": "Nodes registered", "total_nodes": list(blockchain.nodes)}

@app.get("/nodes/resolve")
def resolve_conflicts():
    replaced = blockchain.resolve_conflicts()
    if replaced:
        return {
            "message": "Our chain was replaced",
            "new_chain": [block.to_dict() for block in blockchain.chain]
        }
    else:
        return {
            "message": "Our chain is authoritative",
            "chain": [block.to_dict() for block in blockchain.chain]
        }
