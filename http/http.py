# -*- coding: cp1251 -*-

import urllib2
import sys


if len(sys.argv) < 2:
    exit()
    
url = sys.argv[1]



print urllib2.urlopen(url).readlines()

