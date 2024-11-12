from flask import Flask, request, jsonify, make_response
from flask_mail import Mail, Message
from flask_cors import CORS
from config import Config
import re

app = Flask(__name__)
app.config.from_object(Config)

# Configure CORS
CORS(app)

mail = Mail(app)

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/send_email', methods=['OPTIONS', 'POST'])
def send_email():
    # Handle preflight OPTIONS request for CORS
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response, 200

    # POST request handling for email functionality
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
            recipients=[app.config['MAIL_USERNAME']],
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
        )
        mail.send(msg)
        return jsonify({"success": "Email sent successfully!"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
