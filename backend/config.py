import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# config.py
import os

class Config:
    MAIL_SERVER = os.getenv("MAIL_SERVER")  # e.g., "smtp.gmail.com"
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))  # Port number, commonly 587 for TLS
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true").lower() == "true"
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", "false").lower() == "true"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")  # Your email username
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")  # Your email password
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")  # Default sender email
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')


