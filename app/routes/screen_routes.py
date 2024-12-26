from flask import Blueprint, jsonify, request
from app.models import db, Screen
from pickle import dumps, loads

screen_routes = Blueprint('screen_routes', __name__)

@screen_routes.route('/screen/<int:id>', methods=['GET'])
def get_screens():
    screens = Screen.query().filter_by(theater_id=id).all()
    print(screens)

@screen_routes.route('/screen/<int:id>', methods=['POST'])
def add_screen(id):
    data = request.json
    type = data.get('type')
    price = data.get('price')
    seats = dumps([seat for seat in range(1,data.get('seats')+1)])
    theater_id = id
    new_screen = Screen(type=type, price=price, seats=seats, theater_id=theater_id)
    db.session.add(new_screen)
    db.session.commit()
    return jsonify({
        'id': new_screen.id,
        'type': new_screen.type,
        'price': new_screen.price,
        'seats': loads(new_screen.seats),
        'theater_id': new_screen.theater_id
    })