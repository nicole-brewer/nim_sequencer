
import subprocess
import os

class Command:

	
	def __init__(self, name, parser, exe):
		self.name = name
		self.parser = parser
		self.exe = exe		
		self.path = os.path.dirname(os.path.realpath(__file__));

	def parse(self, args):

		# We parse the args, which gives us a Namespace object. We turn that
		# into a dictionary and then get a list of just the values.
		# Finally we convert all the values in the list to strings, because
		# thats what subprocess.Popen requires 
		temp = (vars(self.parser.parse_args(args))).values()
		for item in temp:
			args.append(str(item))
		return args

	def run(self, args, parse=True):
		
		# for the sake of modular testing, we need a way to run without parsing
		if parse is True:
			args = self.parse(args)
			
		# dir_path is the directory containing the class file
		# cwd indicates the directory we want to cd into before execution.
		cwd = self.path + '/' + self.name + '/'

		# exe is the location of the executable
		exe = cwd + self.exe

		# We change to the command directory before calling the executable, and
 		# make sure to change back before exiting the method. subprocess.Popen() has
		# parameter options for this but I had trouble getting child processes
		# to terminate
		current_dir = os.getcwd()
		os.chdir(cwd)
		subprocess.check_call(args, executable=exe) #Popen(args, executable=exe, cwd=cwd)
		os.chdir(current_dir)
