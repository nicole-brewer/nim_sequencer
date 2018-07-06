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
