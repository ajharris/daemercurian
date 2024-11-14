import unittest
from dotenv import load_dotenv
from backend.app import create_app  # Correct import
from unittest.mock import patch
import time, os, sys

# Load environment variables
load_dotenv()

print("PYTHONPATH:", os.getenv("PYTHONPATH"))
print("System path:", sys.path)

class TestEnvironmentVariables(unittest.TestCase):
    def test_pythonpath_set(self):
        pythonpath = os.getenv("PYTHONPATH")
        self.assertIsNotNone(pythonpath, "PYTHONPATH is not set")


class EnvTest(unittest.TestCase):
    def test_env_variables(self):
        required_vars = ["MAIL_SERVER", "MAIL_PORT", "MAIL_USERNAME", "MAIL_PASSWORD"]
        for var in required_vars:
            self.assertIsNotNone(os.getenv(var), f"{var} is not set in .env file")


class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

        # Mock `mail.send`
        patcher = patch("backend.app.mail.send")
        self.mock_send = patcher.start()
        self.mock_send.return_value = True
        self.addCleanup(patcher.stop)

    def test_cors_headers(self):
        response = self.app.options('/send_email')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Access-Control-Allow-Origin', response.headers)

    def test_send_email_success(self):
        response = self.app.post('/send_email', json={
            "name": "Test User", "email": "testuser@example.com", "message": "Hello!"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Email sent successfully", response.data)

    def test_invalid_email_format(self):
        response = self.app.post('/send_email', json={
            "name": "User", "email": "invalid-email", "message": "Hello!"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Invalid email format", response.data)

    def test_response_time(self):
        start = time.time()
        response = self.app.post('/send_email', json={
            "name": "Test User", "email": "testuser@example.com", "message": "Hello!"
        })
        end = time.time()
        self.assertLess(end - start, 5)  # response within 5 seconds
        self.assertEqual(response.status_code, 200)

    def test_missing_name_field(self):
        response = self.app.post('/send_email', json={
            "email": "testuser@example.com", "message": "Hello!"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Missing information", response.data)

    def test_missing_email_field(self):
        response = self.app.post('/send_email', json={
            "name": "Test User", "message": "Hello!"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Missing information", response.data)

    def test_missing_message_field(self):
        response = self.app.post('/send_email', json={
            "name": "Test User", "email": "testuser@example.com"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Missing information", response.data)
    
    def test_unusual_but_valid_email_format(self):
        response = self.app.post('/send_email', json={
            "name": "Edge Case User", "email": "user+test@example.co.uk", "message": "Hello!"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Email sent successfully", response.data)
    
    def test_invalid_email_missing_at_symbol(self):
        response = self.app.post('/send_email', json={
            "name": "User", "email": "invalid-email.com", "message": "Hello!"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Invalid email format", response.data)
    
    def test_actual_email_send(self):
        self.mock_send.stop()
        
        try:
            response = self.app.post('/send_email', json={
                "name": "Real User", "email": "realuser@example.com", "message": "This is a real test message."
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Email sent successfully", response.data)
        finally:
            self.mock_send.start()

if __name__ == "__main__":
    unittest.main()
