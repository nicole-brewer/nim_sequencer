import sys
import os
import argparse 
from importlib import import_module
import nim_sequencer as nim
from nim_sequencer.command import Command

__version__ = "0.0.0"

def main():

	nim = Nim()
	nim.run(sys.argv[1:])

class Nim(Command):

	def __init__(self):
		
		# get subdirectories of $NIM/nim_sequencer/nim_sequencer/commands
		self.commands = os.walk(nim.ROOT).next()[1]
		parser = argparse.ArgumentParser( description='Calculate periodicity in nim sequenes', usage='nim [--version] <command> [<args>]\n\n' + 'Nim commands are:\n\t\t\n\tcount\tcounts lines for a maximum in the data documents')
		parser.add_argument('command', choices=self.commands)
		parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version='version ' + __version__)) 	
		Command.__init__(self, parser, nim.ROOT)


	def parse(self, args):
		return super(Nim, self).parse(args)

	def run(self, args, parse=True):
		if parse is True:
			command_name = self.parse([args[0]])
		for command in self.commands:
			if command == command_name[0]:
				module = import_module('nim_sequencer.%s.%s' % (command, command))
				print(module)
				instance = getattr(module, command.title())()	
				instance.run(args[1:])
