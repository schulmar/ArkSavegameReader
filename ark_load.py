#!/usr/bin/python3
import sys
if len(sys.argv) < 1:
	print("Call {0} <path-to-savefile>".format(sys.argv[0]))
	return -1
f = file(sys.argv[1], 'rb')

