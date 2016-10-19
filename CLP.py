from sys import argv
import linecache
from collections import deque

def file_len(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

def print_last5(fname):
	line_count = file_len(fname)
	if (line_count==0):
		print ("File is empty")
	elif (line_count<=5):
		with open(fname) as f:
			print f.read(),
	else:
		with open(fname) as f:
			print (''.join(deque(f, 5))),

def main():
	script, filename = argv
	print_last5(filename)

main()