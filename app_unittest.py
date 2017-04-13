import unittest
from app import app
class Tests(unittest.TestCase):
    
    def test_fun1_10_20(self):
        a1=app(10,20)
        expres=30
        actres=a1.fun1()
        self.assertTrue(actres==expres,"fun1 failed for 10,20")
    def test_fun1_str1_str2(self):
        a1=app('str1','str2')
        expres='str1str2'
        actres=a1.fun1()
        self.assertTrue(actres==expres,"fun1 failed for str1,str2")
    def test_fun1_10_str1(self):
        a1=app(10,"str1")
        expres=None
        actres=a1.fun1()
        self.assertTrue(actres==expres,"fun1 failed for 10,str1")
    def test_fun2_10_20(self):
        a1=app(10,20)
        expres=200
        actres=a1.fun2()
        self.assertTrue(actres==expres,"fun2 failed for 10,20")
    def test_fun2_str1_str2(self):
        a1=app('str1','str2')
        expres=None
        actres=a1.fun2()
        self.assertTrue(actres==expres,"fun2 failed for 10,20")

    

if __name__ == "__main__":
    unittest.main()
    