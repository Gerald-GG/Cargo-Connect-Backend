from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_socketio import SocketIO
from config import Config

db = SQLAlchemy()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    socketio.init_app(app)
    CORS(app)

    from .views import user_views, order_views, payment_views, tracking_views
    app.register_blueprint(user_views.bp)
    app.register_blueprint(order_views.bp)
    app.register_blueprint(payment_views.bp)
    app.register_blueprint(tracking_views.bp)

    return app
