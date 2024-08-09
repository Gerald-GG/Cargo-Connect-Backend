from app.models import Order
from app import db

def create_order(user_id):
    order = Order(user_id=user_id, status='pending')
    db.session.add(order)
    db.session.commit()
    return order

def get_order_by_id(order_id):
    return Order.query.get(order_id)
