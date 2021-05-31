import string

charmap = []

for i in range(0,256):
	charmap.append((123*i+18) % 256)

f = open('./msg.enc','r')
ct = f.read()
f.close()
print(ct)
ctb = bytearray.fromhex(ct)

pt = []
for byt in ctb:
	for x in range(0,256):
		if charmap[x] == byt:
			pt.append(x)
print(pt)
pts = []
for i in pt:
	pts.append(chr(i))
print("".join(pts))
