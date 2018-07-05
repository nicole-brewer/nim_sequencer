import nim_sequencer
import subprocess
import os

class Command(object):
	
	def __init__(self, parser, path):
		self.parser = parser
		self.path = path

	def parse(self, args):

		# We parse the args, which gives us a Namespace object. We turn that
		# into a dictionary and then get a list of just the values.
		# Finally we convert all the values in the list to strings, because
		# thats what subprocess.Popen requires 
		temp = (vars(self.parser.parse_args(args))).values()
		for item in temp:
			args.append(str(item))
		return args

	# can be used to start a process
	def run(self, args, exe, parse=True, background=False):
	
		# for the sake of modular testing, we need a way to run without parsing
		if parse is True:
			args = self.parse(args)
		
		# dir_path is the directory containing the class file
		# cwd indicates the directory we want to cd into before execution.
		cwd = self.path

		# exe is the location of the executable
		exe = os.path.join(cwd, exe)

		# puts the child in it's own process group so the program will
		# continue without waiting for the child to terminate
		if background:
			subprocess.Popen(args, executable=exe, cwd=cwd, preexec_fn=os.setpgrp)
		else:
			return subprocess.check_output(args, executable=exe, cwd=cwd, stdout=PIPE, universal_newlines=True)
