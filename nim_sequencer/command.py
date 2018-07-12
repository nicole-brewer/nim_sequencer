import nim_sequencer
import subprocess
import os

class Command(object):
	
	def __init__(self, parser):
		self.parser = parser
		
	def args_list(self, args):

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

	def run(self, args, background=True, timeout=None):

		if timeout is not None and timeout != 0:
			temp = ['timeout', str(timeout)]
			temp.extend(args)
			args = temp
	
		if background:
			nim_sequencer.daemon.spawn_subprocess(args)
		else:
			subprocess.call(args, cwd=nim_sequencer.dir.BIN, universal_newlines=True)
