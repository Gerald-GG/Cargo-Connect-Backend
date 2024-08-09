# app/views/__init__.py
from .payment_views import bp as payment_bp
from .tracking_views import bp as tracking_bp
from .order_views import bp as order_bp
from .user_views import bp as user_bp

__all__ = ['payment_bp', 'tracking_bp', 'order_bp', 'user_bp']
