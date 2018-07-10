# other
import sys
import argparse
import os
from scipy.special import comb
from subprocess import Popen, PIPE, check_output
from select import select
# nim_sequencer
import nim_sequencer as nim
from nim_sequencer.command import Command
from nim_sequencer.helpers import count_input
from nim_sequencer.wc import wc
from nim_sequencer.valid_walltime import valid_walltime
from nim_sequencer.expect import expect_in
class Input(Command):
	
	def __init__(self):
		parser = argparse.ArgumentParser(prog='nim input', description="creates and shuffles input data")
		parser.add_argument('maximum', type=int, help='the largest element of the subtraction set')
		parser.add_argument('-w', '--walltime', type=valid_walltime, help='walltime format is HH:MM:SS')
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
"""
		if hasattr(args, 'walltime'):
			walltime = str(sum(x * int(t) for x, t in zip([3600, 60, 1], args.walltime.split(":"))))	
			pipein = Popen(['timeout', walltime, '-s'], stdout=PIPE, preexec_fun=os.setpgrp, universal_newlines=True)"""
