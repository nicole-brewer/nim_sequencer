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
		args = []
		for item in temp:
			if item is not None:
				args.append(str(item))
		return args

	# can be used to start a process
	def run_exe(self, args, exe=None, stdin=None, background=False, timeout=0):
	
		# dir_path is the directory containing the class file
		# cwd indicates the directory we want to cd into before execution.
		cwd = self.path
	
		# exe is the location of the executable
		if exe is not None:
			exe = os.path.join(cwd, exe)

		# puts the child in it's own process group so the program will
		# continue without waiting for the child to terminate
		if background:
			subprocess.Popen(args, executable=exe, cwd=cwd, preexec_fn=os.setpgrp, universal_newlines=False)
		else:
			return subprocess.check_output(args, executable=exe, cwd=cwd)
