from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
from .config import Config
from .routes import email_routes  # Import the blueprint from email_routes

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Configure extensions
    CORS(app)
    mail.init_app(app)
    
    # Register blueprints
    app.register_blueprint(email_routes)

    return app
