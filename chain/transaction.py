from dataclasses import dataclass

@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float

    def to_dict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }