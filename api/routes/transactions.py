from flask import Blueprint, request, jsonify
from chain.chain import Blockchain
bp = Blueprint('transactions', __name__)

blockchain = Blockchain()

@bp.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    return jsonify({'message': f'Transaction will be added to Block {index}'}), 201
