# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from config import Config

db = SQLAlchemy()
socketio = SocketIO()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    socketio.init_app(app)

    from app.views import payment_bp, tracking_bp, order_bp, user_bp
    app.register_blueprint(payment_bp, url_prefix='/api')
    app.register_blueprint(tracking_bp, url_prefix='/api')
    app.register_blueprint(order_bp, url_prefix='/api')
    app.register_blueprint(user_bp, url_prefix='/api')

    return app
