import argparse
import os
from nim_sequencer.command import Command
from scipy.special import comb
import multiprocessing as mp
import subprocess
import nim_sequencer as ns

class Count(Command):
	
	def __init__(self):
		parser = argparse.ArgumentParser( description="counts lines in data files")
		parser.add_argument('maximum', type=int, help='the largest element of the subtraction set')
		exe = 'count.sh'
		path = os.path.dirname(os.path.realpath(__file__))
		Command.__init__(self, parser, path)

	def run(self, args):
		Command.run(self, args, 'count.sh', background=True)

	# taken from https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
	# Faster than a subprocess
	def wc(filename):
		f = open(filename, 'rb')
		lines = 0
		buf_size = 1024 * 1024
		read_f = f.raw.read

		buf = read_f(buf_size)
		while buf:
			lines += buf.count(b'\n')
 			buf = read_f(buf_size)

		return lines
