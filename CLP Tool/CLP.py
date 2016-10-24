from sys import argv
import linecache
from collections import deque
import sys
import os
from binaryornot.check import is_binary

def file_type(fname):
	ftype=is_binary(fname)
	if (ftype==True):
		sys.stdout.write ("Sorry, binary files are not supported")
		return False
	else:
		return True

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
	try:
		script, filename = argv
		if (file_type(filename)):
			print_last5(filename)
	except ValueError:
		sys.stderr.write ("No file specified")
	except IOError as (errno, strerror):
		sys.stderr.write ("I/O error({0}): {1}".format(errno, strerror))
	except:
		sys.stderr.write ("Unexpected error:", sys.exc_info()[0])
		raise
	

main()