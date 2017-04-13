import unittest
from app import app
class Tests(unittest.TestCase):
    def setUp(self):
        self.a1=app(10,20)
    
    def test_fun1_10_20(self):
        expres=30
        actres=self.a1.fun1()
        self.assertTrue(actres==expres,"fun1 failed for 10,20")
    
    
    def test_fun2_10_20(self):
        expres=200
        actres=self.a1.fun2()
        self.assertTrue(actres==expres,"fun2 failed for 10,20")
   
    

if __name__ == "__main__":
    unittest.main()
    