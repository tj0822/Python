import unittest
import site
site.addsitedir("..")
from tests.root_path import LibmeTestCase

def suite():
    suite_set = unittest.TestSuite()
    suite_set.addTest(LibmeTestCase("testRootpath"))
    return suite_set

if __name__ == "__main__":
    tests = suite()
    runner=unittest.TextTestRunner()
    runner.run(tests)
