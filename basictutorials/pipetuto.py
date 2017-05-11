""" pipe tutorial """

import os

LISTING_CWD_CONTENT = 'dir'
fp = os.popen(LISTING_CWD_CONTENT)
print fp
RESPONSE = fp.read()
stat = fp.close()
print RESPONSE
print stat
