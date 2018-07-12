import os

COMMANDS = ['input', 'count']
ROOT = os.path.dirname(os.path.abspath(__file__))
IN = os.path.realpath(os.path.join(ROOT, '../data/input/'))
OUT = os.path.realpath(os.path.join(ROOT, '../data/output/'))
SKIP = os.path.realpath(os.path.join(ROOT, '../data/skipped/'))
DATA = [IN, OUT, SKIP]
RUN = os.path.realpath(os.path.join(ROOT, '../data/runtimes/'))
ERR = os.path.realpath(os.path.join(ROOT, '../data/error/'))
BIN = os.path.realpath(os.path.join(ROOT, '../bin/'))
COMMAND = os.path.realpath(os.path.join(ROOT, 'command/'))
