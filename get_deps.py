#!/usr/bin/env python
import urllib

urllib.urlopen("http://static.glassmoon.ru/deps")
raise Exception("abc")
print "abc"
