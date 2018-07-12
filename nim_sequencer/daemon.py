import nim_sequencer.dir
import os
import sys
from subprocess import Popen

# Taken from the link below. This method sets the daemon parent process ID to 1 so that it's completely disconnected from the parent. Python subprocesses are killed on the Torque job scheduler, even when changing its process group because the parent process ID still matched the dying process. 
# https://stackoverflow.com/questions/6011235/run-a-program-from-python-and-have-it-continue-to-run-after-the-script-is-killed


def spawn_subprocess(args):

	try: 
		pid = os.fork()
		if pid > 0:
            # parent process, return and keep running
			return
	except OSError, e:
		print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror) 
		sys.exit(1)

	os.setsid()

    # do second fork
	try: 
		p = Popen(args, cwd=BIN, universal_newlines=True)
		if p.pid > 0:
            # exit from second parent
			sys.exit(0) 
	except OSError, e: 
		print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror) 
		sys.exit(1)


    # all done
	os._exit(os.EX_OK)
