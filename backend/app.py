# backend/app.py

from flask import Flask, send_from_directory
from flask_mail import Mail
from .config import Config
import os

mail = Mail()  # Initialize mail here globally

def create_app():
    app = Flask(__name__, static_folder="build", static_url_path="")
    app.config.from_object(Config)

    # Initialize mail within the app context
    mail.init_app(app)

    # Register blueprints
    from backend.routes.email_routes import email_routes
    app.register_blueprint(email_routes)

    # Serve React App
    @app.route("/")
    @app.route("/<path:path>")
    def serve_react_app(path=""):
        if path != "" and os.path.exists(app.static_folder + "/" + path):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, "index.html")

    return app
