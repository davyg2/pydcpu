import struct

NEXTWORD = list(range(0x10,0x7)) + [0x1e, 0x1f]

def myhex(x):
	x = hex(x)
	x = x[2:]
	x = (4-len(x))*'0' + x
	return x

def strData(data):
	n = int(len(data)/2)
	data = struct.unpack("H"*n, data)
	r = ""
	for i in range(0, int(n/8)):
		r += myhex(i*8) + ": " + " ".join(map(myhex,data[i*8:i*8+8])) + "\n"
	r += myhex(int(n/8)*8) + ": " + " ".join(map(myhex,data[int(n/8)*8:])) + "\n"
	return r

def extract(data):
	return (data & 0xf,(data & 0x3f0) >> 4, (data & 0xfc00) >> 10)

def size(data):
	op, a ,b = extract(data)
	s = 1
	if a in NEXTWORD:
		s += 1
	if b in NEXTWORD:
		s += 1
	return s

	
