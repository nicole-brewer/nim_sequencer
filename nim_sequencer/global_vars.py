import os

ROOT = os.path.dirname(os.path.abspath(__file__))
IN = os.path.realpath(os.path.join(ROOT, '../data/input/'))
OUT = os.path.realpath(os.path.join(ROOT, '../data/output/'))
SKIP = os.path.realpath(os.path.join(ROOT, '../data/skipped/'))
RUN = os.path.realpath(os.path.join(ROOT, '../data/runtimes/'))
DATA = [ IN, OUT, SKIP]
COMMANDS = os.path.realpath(os.path.join(ROOT, 'commands/'))
