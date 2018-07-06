# other
import argparse
import os
from scipy.special import comb
# nim_sequencer
import nim_sequencer as nim
from nim_sequencer.command import Command
from nim_sequencer.helpers import get_data_files
# nim_sequencer.count
from nim_sequencer.count.wc import wc

class Count(Command):
	
	def __init__(self):
		parser = argparse.ArgumentParser( description="counts lines in data files")
		parser.add_argument('maximum', type=int, help='the largest element of the subtraction set')
		exe = 'count.sh'
		path = os.path.dirname(os.path.realpath(__file__))
		Command.__init__(self, parser, path)

	def run(self, args, parse=True):
		if parse:
			args = self.parser.parse_args(args)

		print("|-------- Count Lines: max %s --------|" % args.maximum)
		files = get_data_files(args.maximum)
		print("    Input:\n          actual:   %s\n          expected: %s" % (wc(files[0]), comb(args.maximum - 1, 3, exact=True)))
		out = wc(files[1])
		skip = wc(files[2])
		print("    Output:\n          actual:   %s = %s + %s\n          expected: %s" % (out + skip, out, skip, comb(args.maximum, 4, exact=True)))
		print("|---------------------------------------|")
