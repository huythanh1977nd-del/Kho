from flask import Flask, request, jsonify
from waitress import serve
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Bank Deposit Server is running"
    })


@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Invalid JSON"
        }), 400

    account = data.get("account")
    amount = data.get("amount")
    transaction_id = data.get("transaction_id")

    if not account or amount is None:
        return jsonify({
            "status": "error",
            "message": "Missing account or amount"
        }), 400

    print("===== DEPOSIT =====")
    print("Account:", account)
    print("Amount:", amount)
    print("Transaction:", transaction_id)

    return jsonify({
        "status": "success",
        "message": "Deposit received",
        "account": account,
        "amount": amount,
        "transaction_id": transaction_id
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    serve(app, host="0.0.0.0", port=port)
