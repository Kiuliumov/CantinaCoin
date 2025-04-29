import hashlib
import json
from dataclasses import dataclass, field
from typing import List, Optional
from transaction import Transaction

@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Transaction]
    proof: int
    previous_hash: str
    hash: Optional[str] = field(init=False)

