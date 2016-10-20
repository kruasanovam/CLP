from sys import argv
import linecache
from collections import deque
import sys
import os

def file_len(fname):
	with open(fname) as f:
		i=0
		for i, l in enumerate(f):
			pass
	return i + 1

def print_last5(fname):
	line_count = file_len(fname)
	if (os.stat(fname).st_size == 0):
		sys.stdout.write ("File is empty")
	elif (line_count<=5):
		with open(fname) as f:
			sys.stdout.write (f.read())
	else:
		with open(fname) as f:
			sys.stdout.write (''.join(deque(f, 5)))

def main():
	script, filename = argv
	print_last5(filename)

main()