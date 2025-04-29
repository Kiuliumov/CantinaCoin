import time
from typing import List
from .block import Block, Transaction
from .proof import proof_of_work
import hashlib

class Blockchain:
    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = []
        self.current_transactions: List[Transaction] = []
        self.difficulty = difficulty

        print("Creating genesis block...")
        self.new_block(previous_hash="1", proof=100)

    def new_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Creates a new transaction in the list of transactions.

        :return: The index of the block that will hold this transaction.
        """
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)
        return self.last_block.index + 1

    def new_block(self, proof: int, previous_hash: str = None) -> Block:
        """
        Creates a new block and adds it to the chain.

        :param proof: <int> The proof given by the proof of work algorithm
        :param previous_hash: (Optional) Hash of previous block
        :return: <Block> The new block
        """
        block = Block(
            index=len(self.chain) + 1,
            timestamp=time.time(),
            transactions=self.current_transactions.copy(),
            proof=proof,
            previous_hash=previous_hash or self.last_block.hash
        )

        self.current_transactions = []
        self.chain.append(block)
        return block

    def mine_block(self) -> Block:
        """
        Mines a new block using proof of work and adds it to the chain.
        """
        last_proof = self.last_block.proof
        proof = proof_of_work(last_proof, self.difficulty)
        return self.new_block(proof)

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def is_chain_valid(self) -> bool:
        """
        Checks if the entire blockchain is valid.

        :return: <bool> True if valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.previous_hash != previous.hash:
                return False

            if current.hash != current.compute_hash():
                return False

            guess = f"{previous.proof}{current.proof}".encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            if guess_hash[:self.difficulty] != "0" * self.difficulty:
                return False

        return True
