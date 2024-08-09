# app/views/tracking_views.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import Tracking

bp = Blueprint('tracking', __name__)

@bp.route('/tracking/<int:id>', methods=['GET'])
def get_tracking(id):
    tracking = Tracking.query.get_or_404(id)
    return jsonify({
        'id': tracking.id,
        'status': tracking.status,
        'location': tracking.location
    })
