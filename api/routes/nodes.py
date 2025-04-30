from flask import Blueprint, request, jsonify
from urllib.parse import urlparse

bp = Blueprint('nodes', __name__)

nodes = set()


@bp.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()
    urls = values.get('nodes')

    if urls is None:
        return "Error: Please supply a list of node URLs", 400

    for url in urls:
        parsed_url = urlparse(url)

        if parsed_url.scheme and parsed_url.netloc:
            nodes.add(url)
        else:
            return f"Error: Invalid URL {url}", 400

    return jsonify({'message': 'Nodes added', 'nodes': list(nodes)}), 201
