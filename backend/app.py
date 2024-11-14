# backend/app.py

from flask import Flask
from flask_mail import Mail
from .config import Config

mail = Mail()  # Initialize mail here globally

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize mail within the app context
    mail.init_app(app)

    # Register blueprints
    from backend.routes.email_routes import email_routes
    app.register_blueprint(email_routes)

    return app
