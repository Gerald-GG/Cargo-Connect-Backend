# app/views/user_views.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import User

bp = Blueprint('user', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first() is not None:
        return jsonify({'message': 'Username already exists'}), 400
    if User.query.filter_by(email=data['email']).first() is not None:
        return jsonify({'message': 'Email already exists'}), 400

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])  # Assuming you have a set_password method to hash the password
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201
