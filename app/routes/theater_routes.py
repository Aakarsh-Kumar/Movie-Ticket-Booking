from flask import Blueprint, jsonify, request
from app.models import db, Theater

theater_routes = Blueprint('theater_routes', __name__)

@theater_routes.route('/theaters', methods=['GET'])
def get_theaters():
    theaters = Theater.query.all()
    return jsonify([
        {
            'id': theater.id,
            'name': theater.name,
            'location': theater.location
        }
        for theater in theaters
    ])
@theater_routes.route('/theaters', methods=['POST'])
def add_theaters():
    data = request.json
    name = data.get('name')
    location = data.get('location')
    new_theater = Theater(name=name, location=location)
    db.session.add(new_theater)
    db.session.commit()
    return jsonify({
        'id': new_theater.id,
        'name': new_theater.name,
        'location': new_theater.location
    })