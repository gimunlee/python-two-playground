"""Class tutorial"""
from time import time

def func1(self, first, second):
    """Returns True when first is less than second"""
    print self.body
    return first < second

class Class1(object):
    """Test class 1"""
    sharedList = []
    func = func1
    @staticmethod
    def gunc():
        """Says hello g"""
        return 'hello g'
    hunc = gunc
    def __init__(self, left, right):
        self.body = left + right
        self.sharedList.append(time())
    @staticmethod
    def __private_method():
        """A private method"""
        print 'private'
class Dlass(Class1):
    """Test class 2"""
    @staticmethod
    def __private_method():
        """A private method"""
        print 'private'

INSTANCE1 = Class1(1, 2)
print INSTANCE1.func(4, 5)
print Class1.sharedList

INSTANCE2 = Class1(3, 4)
print INSTANCE1.func(4, 5)
print INSTANCE2.func(3, 4)
print Class1.sharedList

INSTANCE1._Class1__private_method()
print [x for x in dir(INSTANCE1) if x.rfind('__') < len(x)-2]
try:
    INSTANCE1.__private_method()
except AttributeError, attribute_error:
    print attribute_error

INSTANCE3 = Dlass(1, 2)
print [x for x in dir(INSTANCE3) if x.rfind('__') < len(x)-2]
INSTANCE3._Class1__private_method()
INSTANCE3._Dlass__private_method()
