
"""
Proof of Work algorithm.

Adapted from: Daniel van Flymen's educational blockchain tutorial (Hackernoon)
Original concept: Proof of Work from the Bitcoin whitepaper by Satoshi Nakamoto (2008)
https://bitcoin.org/bitcoin.pdf
"""

import hashlib

def proof_of_work(last_proof: int, difficulty: int = 4) -> int:
    """
    Simple Proof of Work algorithm:
    - Find a number 'proof' such that hash(last_proof + proof) contains `difficulty` leading zeros.

    :param last_proof: <int> Previous block's proof
    :param difficulty: <int> Number of leading zeros required in hash
    :return: <int> New valid proof
    """
    proof = 0
    print(f"Starting proof of work (difficulty: {difficulty})...")

    while not valid_proof(last_proof, proof, difficulty):
        proof += 1

    print(f"Proof of work found: {proof}")
    return proof

def valid_proof(last_proof: int, proof: int, difficulty: int = 4) -> bool:
    """
    Validates the proof by checking if hash(last_proof + proof) contains `difficulty` leading zeros.

    :param last_proof: <int> Previous block's proof
    :param proof: <int> Current guess
    :param difficulty: <int> Difficulty level
    :return: <bool> True if correct, False otherwise
    """
    guess = f"{last_proof}{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:difficulty] == "0" * difficulty
