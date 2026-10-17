"""Account routes"""
from flask import jsonify, request, make_response, abort
from service import app
from service.models import db, Account


@app.route("/")
def index():
    """Index"""
    return jsonify(name="Account REST API Service", version="1.0"), 200


@app.route("/accounts", methods=["POST"])
def create_accounts():
    """CREATE"""
    account = Account()
    account.deserialize(request.get_json())
    db.session.add(account)
    db.session.commit()
    location_url = f"/accounts/{account.id}"
    return make_response(jsonify(account.serialize()), 201,
                         {"Location": location_url})


@app.route("/accounts", methods=["GET"])
def list_accounts():
    """LIST"""
    return jsonify([a.serialize() for a in Account.query.all()]), 200


@app.route("/accounts/<int:account_id>", methods=["GET"])
def read_accounts(account_id):
    """READ"""
    account = db.session.get(Account, account_id)
    if not account:
        abort(404, f"Account {account_id} not found")
    return jsonify(account.serialize()), 200


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
    """UPDATE"""
    account = db.session.get(Account, account_id)
    if not account:
        abort(404, f"Account {account_id} not found")
    account.deserialize(request.get_json())
    db.session.commit()
    return jsonify(account.serialize()), 200


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_accounts(account_id):
    """DELETE"""
    account = db.session.get(Account, account_id)
    if account:
        db.session.delete(account)
        db.session.commit()
    return "", 204
