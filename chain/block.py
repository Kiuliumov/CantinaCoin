import hashlib
import json
from dataclasses import dataclass, field
from typing import List, Optional
from chain.transaction import Transaction

@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Transaction]
    proof: int
    previous_hash: str
    hash: Optional[str] = field(init=False)

    def __post_init__(self):
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        Generate SHA-256 hash of the block's contents.
        Excludes the hash field itself.
        """
        block_data = {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [t.__dict__ for t in self.transactions],
            'proof': self.proof,
            'previous_hash': self.previous_hash
        }
        block_string = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'proof': self.proof,
            'previous_hash': self.previous_hash
        }

    @classmethod
    def from_dict(cls, data: dict):
        transactions = [Transaction(**tx) for tx in data['transactions']]
        return cls(
            index=data['index'],
            timestamp=data['timestamp'],
            transactions=transactions,
            proof=data['proof'],
            previous_hash=data['previous_hash']
        )