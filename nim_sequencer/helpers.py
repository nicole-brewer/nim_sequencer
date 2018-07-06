import nim_sequencer.global_vars
import os

def get_filename(maximum):
	return 'max' + str(maximum) + '.txt'

def get_data_files(maximum):

	files = []
	for path in nim_sequencer.global_vars.DATA:
		files.append(os.path.join(path, 'max' + str(maximum) + '.txt'))
	
	return files
