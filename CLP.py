from sys import argv
import linecache

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def main():
	script, filename = argv
	line_count = file_len(filename)
	if (line_count==0):
		print ("File is empty")
	elif (line_count<=5):
		with open(filename) as f:
		     print f.read(),
	else:
		y=4
		while (y>=0):
			print(linecache.getline(filename, line_count-y)),
			y-=1

main()