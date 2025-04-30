from flask import Flask
from api.routes import blockchain, transactions, nodes, conflict_resolver

def create_app():
    app = Flask(__name__)

    app.register_blueprint(blockchain.bp)
    app.register_blueprint(transactions.bp)
    app.register_blueprint(nodes.bp)
    app.register_blueprint(conflict_resolver.bp)

    return app

app = create_app()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)