# other
import sys
import argparse
import os
from scipy.special import comb
from subprocess import Popen, PIPE, check_output
from select import select
# nim_sequencer
from nim_sequencer.command import Command
from nim_sequencer.helpers import count_input, wc

class Input(Command):
	
	def __init__(self):
		parser = argparse.ArgumentParser(prog='nim input', description="creates and shuffles input data")
		parser.add_argument('maximum', type=int, help='the largest element of the subtraction set')
		path = os.path.dirname(os.path.realpath(__file__))
		Command.__init__(self, parser, path)

	def run(self, args):
		
		error_msg = "nim input: Error: the input file is corrupt\n"
		args = self.parser.parse_args(args)	
		actual, expected, path = count_input(args.maximum)
		sub_args = ['./input3_background.sh']

		# if there are already enought lines in the file, exit the program 	
		if actual > expected:
			sys.stderr.write(error_msg)
			exit()
		elif actual == expected:
			print("Nothing to do: input file already complete")
			exit()

		# if the file isn't yet complete but it already exists then read the last line
		# and start at writing at the next one
		elif os.path.isfile(path) and actual > 0:
			sub_args.extend(check_output(['tail', path, '-n', '1']).strip('\n').split(' '))
			sub_args[3] = str(int(sub_args[3]) + 1)

		# else if the file is nonexistant or empty, start the permutations at "1 2 3"
		else:
			sub_args.extend(['1', '2', '3'])

		# then add the max and the path and start a subprocess in the background
		sub_args.append(str(args.maximum))
		sub_args.append(path)
		Command.run_exe(self, sub_args, background=True)
