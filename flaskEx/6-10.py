class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert b'You were logged in' in rv.get_data()
        rv = self.logout()
        assert b'You were logged out' in rv.get_data()
        rv = self.login('adminx', 'default')
        assert b'Invalid username' in rv.get_data()
        rv = self.login('admin', 'defaultx')
        assert b'Invalid password' in rv.get_data()