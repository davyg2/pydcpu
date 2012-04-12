
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
import util
import dumper

SIZERAM = 0x10000

class Emulateur:
	instr1 = []
	instr2 = []
	arg = []
	regs = "ABCXYZIJ"
	
	def init():
		Emulateur.instr1 = [
			None,
			lambda s,a,b : s.set(a, s[b]),
			lambda s,a,b : s.set(a, s[a] +  s[b]),
			lambda s,a,b : s.set(a, s[a] -  s[b]),
			lambda s,a,b : s.set(a, s[a] *  s[b]),
			lambda s,a,b : s.set(a, s[a] /  s[b]),
			lambda s,a,b : s.set(a, s[a] %  s[b]),
			lambda s,a,b : s.set(a, s[a] << s[b]),
			lambda s,a,b : s.set(a, s[a] >> s[b]),
			lambda s,a,b : s.set(a, s[a] &  s[b]),
			lambda s,a,b : s.set(a, s[a] |  s[b]),
			lambda s,a,b : s.set(a, s[a] ^  s[b]),
			lambda s,a,b : s.test(s[a]==s[b]),
			lambda s,a,b : s.test(s[a]!=s[b]),
			lambda s,a,b : s.test(s[a]>s[b]),
			lambda s,a,b : s.test(s[a]&s[b]!=0),
		]
	
		Emulateur.instr2 = [None, Emulateur.jsr]
	
		Emulateur.arg = \
			[
				lambda s : 'A',
				lambda s : 'B',
				lambda s : 'C',
				lambda s : 'X',
				lambda s : 'Y',
				lambda s : 'Z',
				lambda s : 'I',
				lambda s : 'J',
				lambda s : s['A'],
				lambda s : s['B'],
				lambda s : s['C'],
				lambda s : s['X'],
				lambda s : s['Y'],
				lambda s : s['Z'],
				lambda s : s['I'],
				lambda s : s['J'],
				lambda s : s['A'] + s[s.incr('PC')],
				lambda s : s['B'] + s[s.incr('PC')],
				lambda s : s['C'] + s[s.incr('PC')],
				lambda s : s['X'] + s[s.incr('PC')],
				lambda s : s['Y'] + s[s.incr('PC')],
				lambda s : s['Z'] + s[s.incr('PC')],
				lambda s : s['I'] + s[s.incr('PC')],
				lambda s : s['J'] + s[s.incr('PC')],
				lambda s : s.incr('SP'),
				lambda s : s['SP'],
				lambda s : s.decr('SP'),
				lambda s : 'SP',
				lambda s : 'PC',
				lambda s : 'O',
				lambda s : s[s.incr('PC')],
				lambda s : s.incr('PC'),
		]
	
	def __init__(self, cbVar = None):
		self.registres = dict([(reg, 0) for reg in list(self.regs) + ['PC', 'SP', 'O']])
		self.ram = [0]*SIZERAM
		self.tick = 0
		self.cbVar = cbVar
	
	def getArg(self, arg):
		if arg < 0x20:
			return self.arg[arg](self)
		else:
			self["temp"] = arg-0x20
			return "temp"

	def step(self):
		pc = hex(self['PC'])
		(op, arg1, arg2) = util.extract(self[self.incr('PC')])
		if op==0:
			a = self.getArg(arg2)
			if type(a) == int:
				da = hex(a)
			else:
				da = a
			print("{pc}: {mnem}({op}) {a}({va})".format(
				pc=pc,
				op=hex(arg1),
				mnem=dumper.MNEM2[arg1],
				a=da,
				va=hex(self[a])
			))
			self.instr2[arg1](self, a)
		else:
			a = self.getArg(arg1)
			b = self.getArg(arg2)
			if type(a) == int:
				da = hex(a)
			else:
				da = a
			if type(b) == int:
				db = hex(b)
			else:
				db = b
			
			print("{pc}: {mnem}({op}) {a}({va}), {b}({vb})".format(
				pc=pc,
				op=hex(op),
				mnem=dumper.MNEM1[op],
				a=da,
				va=hex(self[a]),
				b=db,
				vb=hex(self[b])
			))
			self.instr1[op](self, a, b)
	
	def __getitem__(self, item):
		if type(item) == int:
			return self.ram[item]
		else:
			return self.registres[item]
	
	def __setitem__(self, item, v):
		if type(item) == int:
			self.ram[item] = v
		else:
			self.registres[item] = v
		if self.cbVar:
			self.cbVar(item, v)
	
	def set(self, out, data):
		self[out] =  data & 0xffff
		self['O'] = (data & 0xffff0000) >> 16
	
	def incr(self, reg):
		old = self[reg]
		self[reg] = (self[reg] + 1) % SIZERAM
		return old
	
	def decr(self, reg):
		self[reg] = (self[reg] - 1 + SIZERAM) % SIZERAM
		return self[reg]

	def test(self, v):
		if not v:
			self['PC'] += util.size(self[self['PC']])
	
	def jsr(self, a):
		self[self.decr('SP')] = self['PC']
		self['PC'] = self[a]
	
	def start(self):
		while True:
			self.step()

	def load(self, data):
		for i in range(0, int(len(data)/2)):
			self[i] = data[i*2] + data[i*2+1]*0x100
		for x in self.registres:
			self.registres[x] = 0

Emulateur.init()

