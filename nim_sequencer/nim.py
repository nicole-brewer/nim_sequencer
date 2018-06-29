# -*- coding: utf-8 -*-


"""nim.nim: provides entry point main()."""


__version__ = "0.2.0"


import sys
import os
import argparse 
from commands.command import Command

		

			
def main():

	
	base_path = os.path.dirname(os.path.realpath(__file__))


	# COUNT
	count_parser = argparse.ArgumentParser( description="counts lines in data files")
	count_parser.add_argument('maximum', type=int, help='the largest element of the subtraction set')

	commands = {}
	commands['count'] = Command('count', count_parser, 'count.sh')	
	
	parser = argparse.ArgumentParser( description='Calculate periodicity in nim sequenes', usage='nim [--version] <command> [<args>]\n\n' + 'Nim commands are:\n\t\t\n\tcount\tcounts lines for a maximum in the data documents''')
	parser.add_argument('command', choices=commands.keys())
	parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version='version ' + __version__)) 	
	args = vars(parser.parse_args(sys.argv[1:2])).values()
	commands.get(args[0]).run(sys.argv[2:])
