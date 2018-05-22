import unittest
import flask_session

class sessionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flask_session.app.test_client()

    def testSessionRead(self):
        response = self.app.get("/session_read")

        with self.app.session_transaction() as session:
            self.assertEqual(session['foo'], 'bar')

    def testSessionWrite(self):
        write_resp = self.app.get("/session_write")

        with self.app.session_transaction() as session:
            session['foo'] = 'new bar'
            self.assertEqual(session['foo2'], 'bar2')
            self.assertEqual(session['foo'], 'new bar')

if __name__ == "__main__":
    unittest.main()