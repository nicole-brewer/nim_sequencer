import nim_sequencer.global_vars
from scipy.special import comb
import os

def get_filename(maximum):
	return 'max' + str(maximum) + '.txt'


def get_input_file(maximum):
	return os.path.join(nim_sequencer.global_vars.IN, get_filename(maximum))

def get_output_file(maximum):
	return os.path.join(nim_sequencer.global_vars.OUT, get_filename(maximum))

def get_skipped_file(maximum):
	return os.path.join(nim_sequencer.global_vars.SKIP, get_filename(maximum))

def get_data_files(maximum):

	files = []
	for path in nim_sequencer.global_vars.DATA:
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
