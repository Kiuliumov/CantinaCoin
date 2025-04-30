from flask import Blueprint, jsonify
from chain.chain import Blockchain
from chain.block import Block

bp = Blueprint('blockchain', __name__)

blockchain = Blockchain()


@bp.route('/blockchain', methods=['GET'])
def get_blockchain():
    """
    Returns the full blockchain as a JSON response
    """
    blockchain_data = []

    for block in blockchain.chain:
        block_data = {
            'index': block.index,
            'timestamp': block.timestamp,
            'transactions': [
                {'sender': tx.sender, 'recipient': tx.recipient, 'amount': tx.amount}
                for tx in block.transactions
            ],
            'proof': block.proof,
            'previous_hash': block.previous_hash,
            'hash': block.hash,
        }
        blockchain_data.append(block_data)

    return jsonify({
        'length': len(blockchain.chain),
        'chain': blockchain_data
    })