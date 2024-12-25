from flask import Blueprint, jsonify, request
from app.models import db, User
import hashlib

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    password = data['password']
    password = hashlib.sha256(password.encode()).hexdigest()
    user = User(
        name=data['name'],
        email=data['email'],
        password=password
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully', 'user_id': user.id})
