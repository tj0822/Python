import os
import flask_board
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):        
        self.app = flask_board.app.test_client()
        
    def testArticleRead(self):
        read_stat = self.app.get("/board/30", data={"key":"subject"})

        self.assertEqual(read_stat.status_code, 200, '게시판에서 데이터를 읽어오는데 오류가 발생했습니다')

if __name__ == '__main__':
    unittest.main()