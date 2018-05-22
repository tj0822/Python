import unittest

class equalIterator:
	def __iter__(self):
		yield 3

class CountEqualTestCase(unittest.TestCase):

    def testCountEqual(self):
        self.assertCountEqual(equalIterator(), equalIterator())

if __name__ == '__main__':
    unittest.main()