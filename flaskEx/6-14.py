import unittest

class customObject:
    def __init__(self, obj_name):
        self.name = obj_name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return "<customObject %s>" % self.name

class CustomTypeEqualityTestCase(unittest.TestCase):

    def customTypeEqualFunc(self, first, second, msg=None):
        if first != second:
            standardMsg = '%s != %s' % (first, second)
            self.fail(self._formatMessage(msg, standardMsg))

    def setUp(self):        
        self.addTypeEqualityFunc(customObject, 'customTypeEqualFunc')

    def testEqual(self):
        a = customObject('test')
        b = customObject('test2')

        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()