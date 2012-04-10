#!/usr/bin/python3
"""
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2012 Guillaume DAVY <davyg2 at gmail dot com>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.
"""

import parser
import sys
import util

inputfile = None
outputfile = None
verbose = False

for i in range(1, len(sys.argv)):
	if sys.argv[i].startswith("-v"):
		verbose = True
	elif sys.argv[i].startswith("-o"):
		if len(sys.argv[i]) == 2:
			outputfile = sys.argv[i+1]
		else:
			outputfile = sys.argv[i][2:]
	elif outputfile != sys.argv[i]:
		inputfile = sys.argv[i]
if inputfile == None:
	print("Usage: asm [-o output] input")
	exit(0)

if outputfile == None:
	outputfile = "a.out"

parser = parser.Parser()

f = open(inputfile, 'r')
data = parser.parse(f.read())
f.close()

f = open(outputfile, 'wb')
f.write(data)
f.close()

if verbose:
	print(util.strData(data))

