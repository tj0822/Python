import unittest
import libme

class LibmeTestCase(unittest.TestCase):

    def setUp(self):
        self.app = libme.app.test_client()

    def testArticleRead(self):
        read_page = self.app.get("/")

        self.assertIn(b"Hello World!", read_page.get_data(), '예상한 응답이 아닙니다!')

if __name__ == '__main__':
    unittest.main()
