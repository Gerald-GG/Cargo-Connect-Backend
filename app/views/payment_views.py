# app/views/payment_views.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import Payment, Order

bp = Blueprint('payment', __name__)

@bp.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    order = Order.query.get(data['order_id'])
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    payment = Payment(order_id=order.id, amount=data['amount'], status='completed')
    db.session.add(payment)
    db.session.commit()
    return jsonify({'message': 'Payment completed successfully'}), 201

@bp.route('/payments/<int:id>', methods=['GET'])
def get_payment(id):
    payment = Payment.query.get_or_404(id)
    return jsonify({
        'id': payment.id,
        'order_id': payment.order_id,
        'amount': payment.amount,
        'status': payment.status
    })
