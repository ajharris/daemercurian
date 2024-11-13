import unittest
from app import app
from unittest.mock import patch
import time

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Mock `mail.send` for all tests except the one actual email send test
        patcher = patch("app.mail.send")
        self.mock_send = patcher.start()
        self.mock_send.return_value = True
        self.addCleanup(patcher.stop)  # Ensures patch is stopped after each test

    def test_cors_headers(self):
        response = self.app.options('/send_email')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Access-Control-Allow-Origin', response.headers)

    def test_send_email_success(self):
        # This test uses the mocked `mail.send`
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

    def test_actual_email_send(self):
        # Stop the patch temporarily for this test
        self.mock_send.stop()
        
        try:
            response = self.app.post('/send_email', json={
                "name": "Real User", "email": "realuser@example.com", "message": "This is a real test message."
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Email sent successfully", response.data)
        finally:
            # Restart the mock for the remaining tests
            self.mock_send.start()

if __name__ == "__main__":
    unittest.main()
