from PIL import Image
import sys
import binascii

def int2bytes(bits):
	i = int(bits, 2)
	hex_string = '%x' % i
	n = len(hex_string)
	return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

original = Image.open('output.png')
width, height = original.size

bits = ""

outputString = ""
count = 0
for i in range(width):
	for j in range(height):
		if sys.version_info <= (3,0):
			r,g,b,_ = original.getpixel((i, j))
		else:
			r,g,b = original.getpixel((i, j))

		bits += str(r & 1)
		count += 1

		if count == 16:
			count = 0
			if bits != '00000000':
				if sys.version_info <= (3,0):
					outputString += int2bytes(bits)
				else:
					outputString += str(int2bytes(bits))[2]
			bits = ""

print(outputString)