import unittest

class RegexTestCase(unittest.TestCase):

    def testRegex(self):
        self.assertRegex("abbbbc", "a[b]*c")
        self.assertRegex("abbbbc", "a[b]?c")

    def testNotRegex(self):
        self.assertNotRegex("abbbbc", "a[b]*c")
        self.assertNotRegex("abbbbc", "a[b]?c")

if __name__ == '__main__':
    unittest.main()