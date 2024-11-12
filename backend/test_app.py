import unittest
import time
from app import app
from dotenv import load_dotenv
from unittest.mock import patch

# Load environment variables from .env file
load_dotenv()  

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch("app.mail.send", autospec=True)
    def test_send_email_success(self, mock_send):
        # Using mocked `mail.send`
        mock_send.return_value = True
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "testuser@example.com",
            "message": "This is a test message."
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"success", response.data)

    @patch("app.mail.send", autospec=True)
    def test_send_email_cors(self, mock_send):
        # Perform a preflight OPTIONS request with the necessary headers
        response = self.app.options('/send_email', headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "Content-Type"
        })
    
        # Check for CORS headers in the response
        self.assertEqual(response.status_code, 200)
        self.assertIn('Access-Control-Allow-Origin', response.headers)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'], '*')
        self.assertIn('Access-Control-Allow-Methods', response.headers)
        self.assertIn('POST', response.headers['Access-Control-Allow-Methods'])  # Ensure POST method is allowed

    @patch("app.mail.send", autospec=True)
    def test_invalid_email_format(self, mock_send):
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "invalid-email",
            "message": "This is a test message."
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"error", response.data)

    @patch("app.mail.send", autospec=True)
    def test_empty_message_body(self, mock_send):
        response = self.app.post('/send_email', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"error", response.data)

    @patch("app.mail.send", autospec=True)
    def test_send_email_missing_field(self, mock_send):
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "testuser@example.com"
            # Missing "message" field
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"error", response.data)

    @patch("app.mail.send", autospec=True)
    def test_large_message_content(self, mock_send):
        large_message = "a" * 10000  # 10,000 characters
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "testuser@example.com",
            "message": large_message
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"success", response.data)

    @patch("app.mail.send", autospec=True)
    def test_response_time(self, mock_send):
        start_time = time.time()
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "testuser@example.com",
            "message": "This is a test message."
        })
        end_time = time.time()
        response_time = end_time - start_time
        self.assertLess(response_time, 2)  # Ensuring the response is under 2 seconds
        self.assertEqual(response.status_code, 200)

    @patch("app.mail.send", autospec=True)
    def test_email_sending_failure(self, mock_send):
        # Simulate a failure in sending the email
        mock_send.side_effect = Exception("Simulated email failure")
        response = self.app.post('/send_email', json={
            "name": "Test User",
            "email": "testuser@example.com",
            "message": "This is a test message."
        })
        self.assertEqual(response.status_code, 500)
        self.assertIn(b"error", response.data)

    def test_actual_email_send(self):
        # This test sends a real email without any mocking
        response = self.app.post('/send_email', json={
            "name": "Real User",
            "email": "realuser@example.com",
            "message": "This is a real test message."
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"success", response.data)


if __name__ == "__main__":
    unittest.main()
