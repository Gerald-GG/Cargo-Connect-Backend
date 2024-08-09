from app.models import Payment
from app import db

def create_payment(order_id, amount):
    payment = Payment(order_id=order_id, amount=amount, status='completed')
    db.session.add(payment)
    db.session.commit()
    return payment

def get_payment_by_id(payment_id):
    return Payment.query.get(payment_id)
