import sys
import argparse 
from importlib import import_module
from .command import Command
from nim_sequencer.dir import COMMANDS
__version__ = "0.0.0"

def main():

	commands = 	COMMANDS
	parser = argparse.ArgumentParser(description='Calculate periodicity in nim sequenes', usage='nim [--version] <command> [<args>]\n\n' + 'Nim commands are:\n\t\t\n\tcount\tcounts lines for a maximum in the data documents')
	parser.add_argument('command', choices=commands)
	parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version='version ' + __version__)) 	
	ns = parser.parse_args(sys.argv[1:2])
	
	for valid_option in commands:
		if ns.command == valid_option:
			module = import_module('nim_sequencer.commands.%s' % ns.command)
			instance = getattr(module, ns.command.title())()	
			instance.run(sys.argv[2:])
