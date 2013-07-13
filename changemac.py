#!/usr/bin/env python

import sys
from itertools import imap
from random import randint
from os import system

iface = sys.argv[1]
mac = '00:' + ':'.join(['%02x'%x for x in imap(lambda x:randint(0,255), range(5))])
print '\nyour new mac: \n' + mac
try:
    system("ifdown " + iface)
    system("ifconfig " + iface + " hw ether " + mac)
except:
    print 'LOG IN AS ROOT, AND TRY AGAIN!'

finally:
    system("ifup " + iface)
