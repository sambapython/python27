#print fun()
'''
import f1
print f1.fun()
'''
#from f3 import fun1
'''
import f5
print f5.fun()
print f5.fun1()
'''
'''
from f5 import fun,fun1
print fun()
print fun1()
'''
#import module1
#from module1 import file1

#import module2
#print module2.file1.fun1()
#print module2.__init__.file1.fun1()
'''
import module2
print module2.file1.fun()
print module2.file1.fun1()
'''
#from module2 import file1
#import module2
'''
from module2 import file2
print file2.fun1()
'''
'''
import module2
print module2.file1.fun1()
'''
#import module2
'''
import sqlite3
print sqlite3.__file__
import module2
import sys
print sys.path
'''
import module2
print module2.file1.fun()
print module2.file1.fun1()

