import unittest
from ..import init_app
from ..appConfig import config_dict
from ..models import db, User, Short_URL
from flask import Flask


class YourProjectTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app = init_app()

    def test_home_endpoint(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the behavior of the home endpoint

    def test_login_endpoint(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the behavior of the login endpoint

    def test_register_endpoint(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the behavior of the register endpoint

    # Add more test methods to cover other endpoints and functionalities


if __name__ == '__main__':
    unittest.main()
