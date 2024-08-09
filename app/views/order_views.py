# app/views/order_views.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import Order

bp = Blueprint('order', __name__)

@bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order = Order(product=data['product'], quantity=data['quantity'])
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'}), 201

@bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify({
        'id': order.id,
        'product': order.product,
        'quantity': order.quantity
    })
