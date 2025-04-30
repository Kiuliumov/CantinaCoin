from flask import Blueprint, jsonify
import requests
from chain.chain import Blockchain
from chain.transaction import Transaction

bp = Blueprint('consensus', __name__)

blockchain = Blockchain()
nodes = set()

@bp.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = resolve_conflicts()
    if replaced:
        return jsonify({'message': 'Our chain was replaced', 'new_chain': [b.__dict__ for b in blockchain.chain]}), 200
    else:
        return jsonify({'message': 'Our chain is authoritative', 'chain': [b.__dict__ for b in blockchain.chain]}), 200

def resolve_conflicts():
    global blockchain
    new_chain = None
    max_length = len(blockchain.chain)

    for node in nodes:
        try:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                data = response.json()
                length = data['length']
                chain_data = data['chain']

                # Reconstruct the chain from JSON
                chain = []
                for block in chain_data:
                    transactions = [Transaction(**t) for t in block['transactions']]
                    chain.append(Block(
                        index=block['index'],
                        timestamp=block['timestamp'],
                        transactions=transactions,
                        proof=block['proof'],
                        previous_hash=block['previous_hash'],
                    ))

                temp_blockchain = Blockchain()
                temp_blockchain.chain = chain
                if length > max_length and temp_blockchain.is_chain_valid():
                    max_length = length
                    new_chain = temp_blockchain.chain

        except Exception as e:
            print(f"Error contacting node {node}: {e}")

    if new_chain:
        blockchain.chain = new_chain
        return True

    return False