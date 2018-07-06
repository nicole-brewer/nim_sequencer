import os

# taken from https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
# Faster than a subprocess
def wc(filename):

	filename =  os.path.realpath(filename) 

	try:	
		f = open(filename, 'rb')
		lines = 0
		buf_size = 1024 * 1024
		read_f = f.read
		buf = read_f(buf_size)
		while buf:
			lines += buf.count(b'\n')
 			buf = read_f(buf_size)
		return lines
	except IOError:
		return 0

import sys
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Enter a filename when using this program")
	else:
		print("%d lines in %s" % (wc(sys.argv[1]), sys.argv[1]))
