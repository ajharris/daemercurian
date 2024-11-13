import unittest
from app import app
from dotenv import load_dotenv
from unittest.mock import patch

# Load environment variables from .env file
load_dotenv()

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_cors_preflight(self):
        # Test CORS preflight request
        response = self.app.options('/send_email')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Access-Control-Allow-Origin', response.headers)
        self.assertIn('Access-Control-Allow-Methods', response.headers)
        self.assertIn('Access-Control-Allow-Headers', response.headers)

    @patch("app.mail.send")
    def test_send_email_success(self, mock_send):
        # Test successful email send
        mock_send.return_value = True
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "testuser@example.com",
            "message": "This is a test message."
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Email sent successfully", response.data)
        mock_send.assert_called_once()

    def test_invalid_email_format(self):
        # Test invalid email format
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "invalid-email",
            "message": "This is a test message."
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Invalid email format", response.data)

    def test_missing_fields(self):
        # Test missing fields in request
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "message": "Missing email field."
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Missing information", response.data)

    def test_empty_message_content(self):
        # Test empty message content
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "testuser@example.com",
            "message": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Missing information", response.data)

    @patch("app.mail.send")
    def test_send_email_failure(self, mock_send):
        # Simulate email send failure
        mock_send.side_effect = Exception("Simulated email failure")
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "testuser@example.com",
            "message": "This is a test message."
        })
        self.assertEqual(response.status_code, 500)
        self.assertIn(b"error", response.data)

    @patch("app.mail.send")
    def test_large_message_content(self, mock_send):
        # Test sending a large message
        mock_send.return_value = True
        large_message = "a" * 10000  # 10,000 characters
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "testuser@example.com",
            "message": large_message
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Email sent successfully", response.data)

    @patch("app.mail.send")
    def test_response_time(self, mock_send):
        # Mock email sending to avoid network delay
        mock_send.return_value = True
        
        import time
        start_time = time.time()
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "testuser@example.com",
            "message": "This is a test message."
        })
        end_time = time.time()
        response_time = end_time - start_time
        
        # Set a reasonable threshold, like 2 seconds
        self.assertLess(response_time, 2)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
