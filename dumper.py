

MNEM1 = [
			"NBA", "SET", "ADD", "SUB", "MUL", "DIV",
			"MOD", "SHL", "SHR", "AND", "BOR", "XOR",
			"IFE", "IFN", "IFG", "IFB"
		]

MNEM2 = [ "RESERVE", "JSR" ]

"""
class dumper:
	def parseop():
		if self.op==0:
			return (INST2[self.arg1], self.parseArg(self.arg1), None)
		else:
			return (INST1[self.OP], self.parseArg(self.arg1), self.parseArg(self.arg2))
		
		0x0: non-basic instruction - see below
		0x1: SET a, b - sets a to b
		0x2: ADD a, b - sets a to a+b, sets O to 0x0001 if there's an overflow, 0x0 otherwise
		0x3: SUB a, b - sets a to a-b, sets O to 0xffff if there's an underflow, 0x0 otherwise
		0x4: MUL a, b - sets a to a*b, sets O to ((a*b)>>16)&0xffff
		0x5: DIV a, b - sets a to a/b, sets O to ((a<<16)/b)&0xffff. if b==0, sets a and O to 0 instead.
		0x6: MOD a, b - sets a to a%b. if b==0, sets a to 0 instead.
		0x7: SHL a, b - sets a to a<<b, sets O to ((a<<b)>>16)&0xffff
		0x8: SHR a, b - sets a to a>>b, sets O to ((a<<16)>>b)&0xffff
		0x9: AND a, b - sets a to a&b
		0xa: BOR a, b - sets a to a|b
		0xb: XOR a, b - sets a to a^b
		0xc: IFE a, b - performs next instruction only if a==b
		0xd: IFN a, b - performs next instruction only if a!=b
		0xe: IFG a, b - performs next instruction only if a>b
		0xf: IFB a, b - performs next instruction only if (a&b)!=0

	def dump(data):
		self.resultat = []
		self.i = 0
		while self.i < len(data):
			i = self.i
			self.op = data[i] & 0xf
			self.arg1 = (data[i] & 0x3f0) >> 4
			self.arg2 = (data[i] & 0xfc0) >> 10
			self.resultat[i] = self.parseop()
"""
