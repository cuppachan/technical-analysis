#!/usr/bin/python

import sys

def Hello(name):
	if name == 'Alice':
		name = name + '????????'
	name = name + '!!!!!!!'
	print 'Hello' , name 

def main():
	Hello(sys.argv[1])
