import unittest

class AlmostTestCase(unittest.TestCase):

    def testAlmostEqual(self):
        self.assertAlmostEqual(1.1, 1.0, delta=0.2)

    def testNotAlmostEqual(self):
        self.assertNotAlmostEqual(1.1, 1.0, delta=0.1)

if __name__ == '__main__':
    unittest.main()