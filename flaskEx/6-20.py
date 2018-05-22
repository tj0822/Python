import unittest
from flask import session
import flask_session

class sessionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flask_session.app.test_client()

    def testSessionRead(self):
        response = self.app.get("/session_read")

        self.assertEqual(session.get('foo', None), 'bar')

    def testSessionWrite(self):
        self.assertEqual(session.get('foo2', None), None)

        write_resp = self.app.get("/session_write")

        self.assertEqual(session.get('foo2', None), 'bar2')

if __name__ == "__main__":
    unittest.main()