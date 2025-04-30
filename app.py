from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chain.chain import Blockchain

app = FastAPI(title="My Blockchain API")
blockchain = Blockchain()

class TransactionRequest(BaseModel):
    sender: str
    recipient: str
    amount: float

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
