from app.models import Tracking
from app import db

def create_tracking(order_id, location, timestamp):
    tracking = Tracking(order_id=order_id, location=location, timestamp=timestamp)
    db.session.add(tracking)
    db.session.commit()
    return tracking

def get_tracking_by_id(tracking_id):
    return Tracking.query.get(tracking_id)
