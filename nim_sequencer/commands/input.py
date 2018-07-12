# other
import sys
import argparse
import os
from scipy.special import comb
from subprocess import Popen, PIPE, check_output
from select import select
from datetime import timedelta
# nim_sequencer
from nim_sequencer.command import Command
from nim_sequencer.helpers import count_input, wc
from nim_sequencer.daemon import spawn_subprocess

class Input(Command):
	
	def __init__(self):
		parser = argparse.ArgumentParser(prog='nim input', description="creates and shuffles input data")
		parser.add_argument('maximum', type=int, help='the largest element of the subtraction set')
		parser.add_argument('-s', '--seconds', nargs='?', type=int, const=1, default=0, help='the amount of time the program will run in seconds')
		parser.add_argument('-m', '--minutes', nargs='?', type=int, const=1, default=0, help='the amount of time the program will run in minutes')
		parser.add_argument('--hours', nargs='?', type=int, const=1, default=0, help='the amount of time the program will run in hours')
		parser.add_argument('-b', '--background', action='store_true', help = 'spawn a daemon process')
		Command.__init__(self, parser)

	def run(self, args):
	
		error_msg = "nim input: Error: the input file is corrupt\n"
		args = self.parser.parse_args(args)
		time = timedelta(seconds=args.seconds, minutes=args.minutes, hours=args.hours)
		timeout = int(timedelta.total_seconds(time))
		# if time isn't provided, don't timeout the program
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
		before = wc(path)
		Command.run(self, sub_args, background=args.background, timeout=timeout)
		if args.background is not True:
			print("Lines added: %s" % str(wc(path) - before))
