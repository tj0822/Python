import flask_board
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):        
        self.app = flask_board.app.test_client()
        
    def testArticleRead(self):
        read_stat = self.app.get("/board/30")

        self.assertEqual(read_stat.status_code, 200, '게시판에서 데이터를 읽어오는데 오류가 발생했습니다')

    def testEqual(self):
        a = [1,2]
        b = [1,2]

        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()