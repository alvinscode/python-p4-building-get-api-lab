#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    
    
    bakeries = []
    for bakery in Bakery.query.all():
        bakery_list = {
            "id": bakery.id,
            "name": bakery.name,
            "created_at": bakery.created_at
        }
        bakeries.append(bakery_list)

    response = make_response(
        jsonify(bakeries),
        200
    )

    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.get(id)

    if bakery is None:
        return jsonify({"error": "Bakery not found"}), 404

    bakery_list = bakery.to_dict()

    response = make_response(
        jsonify(bakery_list),
        200
    )

    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()

    baked_goods_list = []

    for goods in baked_goods:
        baked_goods_data = goods.to_dict()
        baked_goods_list.append(baked_goods_data)

    response = make_response(
        jsonify(baked_goods_list),
        200
    )

    return response


@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    most_expensive_goods = BakedGood.query.order_by(BakedGood.price.desc()).first()

    if most_expensive_goods is None:
        return jsonify({"error": "No baked goods found"}), 404
    
    most_expensive_goods_data = most_expensive_goods.to_dict()

    response = make_response(
        jsonify(most_expensive_goods_data),
        200
    )

    return response        

if __name__ == '__main__':
    app.run(port=5555, debug=True)
