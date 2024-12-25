from flask import Blueprint, jsonify,request
from app.models import db, Food

food_routes = Blueprint('food_routes', __name__)

@food_routes.route('/food', methods=['GET'])
def get_food():
    food_items = Food.query.all()
    return jsonify([
        {
            'id': food.id,
            'name': food.name,
            'price': food.price
        }
        for food in food_items
    ])
@food_routes.route('/food', methods=['POST'])
def add_food():
    data = request.json
    name = data.get('name')
    price = data.get('price')
    new_food = Food(name=name, price=price)
    db.session.add(new_food)
    db.session.commit()
    return jsonify({
        'id': new_food.id,
        'name': new_food.name,
        'price': new_food.price
    })
