from flask import Blueprint, request, jsonify, make_response
from flask_mail import Message
from ..extensions import mail  # Import mail from extensions
import re

email_routes = Blueprint('email_routes', __name__)

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@email_routes.route('/send_email', methods=['OPTIONS', 'POST'])
def send_email():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response, 200

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message_body = data.get('message')

    if not name or not email or not message_body:
        return jsonify({"error": "Missing information"}), 400

    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    try:
        msg = Message(
            subject=f"New Message from {name}",
            recipients=['your-email@example.com'],
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
        )
        mail.send(msg)
        return jsonify({"success": "Email sent successfully!"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
