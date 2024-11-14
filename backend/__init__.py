from flask import Flask
from .config import Config
from .extensions import mail
from .routes import email_routes  # Import your blueprints here

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    mail.init_app(app)

    # Register blueprints
    app.register_blueprint(email_routes)

    return app
