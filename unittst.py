import unittest
class Tests(unittest.TestCase):
    @staticmethod
    def static_method(a,b):
        pass
    @classmethod
    def setUpClass(cls):
        print "setup class"
    def setUp(self):
        print "setup"
    def test_fun1_10_20(self):
        print "test case1"
    def test_fun1_str1_str2(self):
        print "test vase2"
    def tearDown(self):
        print "teradown"
    @classmethod
    def tearDownClass(cls):
        print "teardownclass"
if __name__ == "__main__":
    unittest.main()
    