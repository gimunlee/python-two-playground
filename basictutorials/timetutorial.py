""" time module tutorials """
import time

print time.time()
print time.localtime(time.time())

import math
print dir(math)

print math.sqrt(256)

help(math.pow)
print math.pow(10, 3)

from time import localtime
print localtime(time.time())

from time import *
print asctime()
