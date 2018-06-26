# -*- coding: utf-8 -*-


"""nim.nim: provides entry point main()."""


__version__ = "0.2.0"


import sys
import argparse
from .stuff import Stuff


def main():

    #print("Executing nim version %s." % __version__)
    #print("List of argument strings: %s" % sys.argv[1:])
    #print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))
    FUNCTION_MAP = {'period' : period }  
    parser = argparse.ArgumentParser(description='Calculate periodicity in nim sequences')
    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version='version ' + __version__))  
    # list(FUNCTION_MAP) is a list of the keys
    parser.add_argument('command', choices=list(FUNCTION_MAP)) 
    args = parser.parse_args()
 
    func = FUNCTION_MAP[args.command]
    func()    
    #args.run(args)

def period():
    print("period")

#usage: git [--version] [--help] [-c name=value]
#           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
#           [-p|--paginate|--no-pager] [--no-replace-objects] [--bare]
#           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
#           <command> [<args>]

class Boo(Stuff):
    pass
