from sys import argv
import linecache

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
		y=4
		while (y>=0):
			print(linecache.getline(fname, line_count-y)),
			y-=1

def main():
	script, filename = argv
	print_last5(filename)

main()