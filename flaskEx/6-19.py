import unittest
from code6_17 import app
from flask import g
from contextlib import contextmanager
from flask import appcontext_pushed

@contextmanager
def user_set(app, user):
    def handler(sender, **kwargs):
        g.user = user
    with appcontext_pushed.connected_to(handler, app):
        yield

class UserInfo:
    def __init__(self, name):
        self.username = name

class UsersMeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def testUsersMe(self):
        user = UserInfo("test")

        with user_set(app, user):
            response = self.app.get("/users/me")

            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()