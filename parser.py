
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
import ply.lex as lex
import ply.yacc as yacc
import struct

class Parser:

	tokens = (
		"INST1",
		"INST2",
		"REG",
		"VIRG",
		"COM",
		"BL",
		"BR",
		"LIT",
		"PLUS",
		"LAB",
		"MOD",
		"SEP"
	)

	t_COM	= r";.*"
	t_LAB	= r":[a-z][a-zA-z]*"
	t_VIRG	= ','
	t_BL	= '\['
	t_BR	= '\]'
	t_PLUS	= '\+'
	t_SEP	= r'\n'


	t_ignore = " \t"

	INST1 = {
		"SET" : 0x01,
		"ADD" : 0x02,
		"SUB" : 0x03,
		"MUL" : 0x04,
		"DIV" : 0x05,
		"MOD" : 0x06,
		"SHL" : 0x07,
		"SHR" : 0x08,
		"AND" : 0x09,
		"BOR" : 0x0a,
		"XOR" : 0x0b,
		"IFE" : 0x0c,
		"IFN" : 0x0d,
		"IFG" : 0x0e,
		"IFB" : 0x0f,
		}

	def t_INST1(self, t):
		r"SET|AND|BOR|XOR|ADD|SUB|MUL|SHR|SHL|DIV|MOD|IFE|IFN|IFG|IFB"
		t.value = self.INST1[t.value]
		return t

	INST2 = {
		"JSR" : 0x01,
	}

	def t_INST2(self, t):
		r"JSR"
		t.value = self.INST2[t.value]
		return t

	MOD = {
		"POP"	: 0x18,
		"PEEK"	: 0x19,
		"PUSH"	: 0x1a,
		"SP"	: 0x1b,
		"PC"	: 0x1c,
		"O"		: 0x1d,
	}

	def t_MOD(self, t):
		r"POP|PEEK|PUSH|SP|PC|O"
		t.value = self.MOD[t.value]
		return t

	REG = {
		"A"	: 0x00,
		"B"	: 0x01,
		"C"	: 0x02,
		"X"	: 0x03,
		"Y"	: 0x04,
		"Z"	: 0x05,
		"I"	: 0x06,
		"J"	: 0x07,
	}

	def t_REG(self, t):
		r"[ABCXYZI]"
		t.value = self.REG[t.value]
		return t

	def t_LIT(self, t):
		r"0x[0-9a-e]+|[a-z][a-zA-z]*|[0-9]+"
		orig = t.value
		if orig[0] in "012345678":
			if len(orig)>1 and orig[1] == 'x':
				t.value = struct.pack("H",int(orig[2:], 16))
			else:
				t.value = struct.pack("H",int(orig))
		else:
			self.todo[self.caddr+1] = t.value
			t.value = '\42\42'.encode()
		return t

	def t_error(self, t):
		raise TypeError("Unknown text '%s'" % (t.value,))
	
	def p_file(self, p):
		"file : ligne SEP file"
		p[0] = p[1] + p[3]
	
	def p_file_vide(self, p):
		"file : "
		p[0] = b""
	
	def p_ligne_0(self, p):
		"ligne : "
		p[0] = b""

	def p_ligne_1(self, p):
		"ligne : LAB instruction COM"
		self.com[self.addr] = p[3][1:]
		self.env[p[1][1:]] = self.addr
		self.addr = self.caddr
		p[0] = p[2]

	def p_ligne_2(self, p):
		"ligne : LAB instruction"
		self.env[p[1][1:]] = self.addr
		self.addr = self.caddr
		p[0] = p[2]

	def p_ligne_3(self, p):
		"ligne : instruction COM"
		self.com[self.addr] = p[2][1:]
		self.addr = self.caddr
		p[0] = p[1]

	def p_ligne_4(self, p):
		"ligne : instruction"
		self.addr = self.curraddr
		p[0] = p[1]

	def p_ligne_5(self, p):
		"ligne : LAB"
		self.env[p[1][1:]] = self.addr
		p[0] = b""

	def p_ligne_6(self, p):
		"ligne : COM"
		self.com[self.addr] = p[1][1:]
		p[0] = b""

	def p_ligne_7(self, p):
		"ligne : LAB COM"
		self.com[self.addr] = p[2][1:]
		self.env[p[1][1:]] = self.addr
		p[0] = b=""

	def p_instruction_1(self, p):
		"""
		instruction : INST1 arg VIRG arg
		"""
		self.caddr += 1
		cmd = struct.pack("H", p[4][0]*0x400 | p[2][0]*0x10 | p[1])
		p[0] = cmd + p[2][1] + p[4][1]
	
	def p_instruction_2(self, p):
		"""
		instruction : INST2 arg
		"""
		self.caddr += 1
		cmd = struct.pack("H", p[2][0]*0x400 | p[1]*0x10)
		p[0] = cmd + p[2][1]

	def p_arg_reg(self, p):
		"""
		arg : REG
		"""
		p[0] = (p[1], b"")

	def p_arg_regmem(self, p):
		"""
		arg : BL REG BR
		"""
		p[0] = (p[2] + 0x08, b"")

	def p_arg_regplus1(self, p):
		"""
		arg : BL LIT PLUS REG BR
		"""
		self.caddr += 1
		p[0] = (p[4] + 0x10, p[2])

	def p_arg_regplus2(self, p):
		"""
		arg : BL REG PLUS LIT BR
		"""
		self.caddr += 1
		p[0] = (p[2] + 0x10, p[4])

	def p_arg_mod(self, p):
		"""arg : MOD
		"""
		p[0] = (p[1], b"")

	def p_arg_litmem(self, p):
		"""
		arg : BL LIT BR
		"""
		self.caddr += 1
		p[0] = (0x1e, p[2])

	def p_arg_lit(self, p):
		"""
		arg : LIT
		"""
		v = struct.unpack('H',p[1])[0]
		if v<=0x1f:
			p[0] = (0x20+v, b"")
			return
		self.caddr += 1
		p[0] = (0x1f, p[1])

	def p_error(self, p):
		raise TypeError("unknown text at %r" % (p.value,))
	
	def __init__(self):
		lex.lex(module=self)
		yacc.yacc(module=self)
	
	def parse(self, data):
		self.addr = 0
		self.caddr = 0
		self.env = {}
		self.todo = {}
		self.com = {}
		r = bytearray(yacc.parse(data))
		for addr, lbl in self.todo.items():
			d = struct.pack("H", self.env[lbl])
			r[2*addr] = d[0]
			r[2*addr+1] = d[1]
		return r


