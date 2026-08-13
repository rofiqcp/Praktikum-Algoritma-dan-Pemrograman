import os
import unittest
from unittest.mock import patch
from app import app


class DeployAppTest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"service aktif", response.data)

    def test_health(self):
        response = self.client.get("/health")
        body = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(body["status"], "ok")
        self.assertIn("service", body)
        self.assertIn("environment", body)

    def test_default_environment(self):
        with patch.dict(os.environ, {}, clear=True):
            response = self.client.get("/health")
            self.assertEqual(response.get_json()["environment"], "development")

    def test_environment_configuration(self):
        with patch.dict(os.environ, {"APP_ENV": "class-demo", "APP_NAME": "Deploy Lab"}, clear=False):
            response = self.client.get("/health")
            body = response.get_json()
            self.assertEqual(body["environment"], "class-demo")
            self.assertEqual(body["service"], "Deploy Lab")

    def test_unknown_route(self):
        self.assertEqual(self.client.get("/route-tidak-ada").status_code, 404)


if __name__ == "__main__":
    unittest.main()
