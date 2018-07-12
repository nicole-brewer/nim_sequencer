from nim_sequencer import dir
from scipy.special import comb
import os

def get_filename(maximum):
	return 'max' + str(maximum) + '.txt'


def get_input_file(maximum):
	return os.path.join(dir.IN, get_filename(maximum))

def get_output_file(maximum):
	return os.path.join(dir.OUT, get_filename(maximum))

def get_skipped_file(maximum):
	return os.path.join(dir.SKIP, get_filename(maximum))

def get_data_files(maximum):

	files = []
	for path in dir.DATA:
		files.append(os.path.join(path, 'max' + str(maximum) + '.txt'))
	
	return files

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

def count_input(maximum):
	filename = get_input_file(maximum)
	return wc(filename), expected_input(maximum), filename

def count_output(maximum):
	filename = get_output_file(maximum)
	return wc(filename), expected_output(maximum), filename

def expected_input(maximum):
	return comb(maximum - 1, 3, exact=True)

def expect_out(maximum):
	return comb(maximum, 4, exact=True)
