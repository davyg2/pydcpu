#!/usr/bin/python3

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

