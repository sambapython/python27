"""
This cell to demonstrate uinttest module
"""
class app:
    """
    App calss
    """
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def fun1(self):
        """
        Provide fun1.
        test case1: 10,20   res=30
        test case1: str2,str1 res=str1str2
        test case1: str1,20   res=None
        test case1: [1,2,3],23   res=None
        """
        try:
            return self.a+self.b
        except:
            return None
    def fun2(self):
        try:
            return self.a*self.b
        except:
            return None
    