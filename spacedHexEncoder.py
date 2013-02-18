# spacedHexEncoder
# By David Gedarovich <dave.gedarovich@gmail.com>
# Takes user input and encodes it to a space-seperated hex file with a matching
# hash file that can be decoded and checked by the second python script.

import hashlib
file = open("output", "w")
hashFile = open("hash", "w")

def encodeText(input):
	i = 0
	for letter in input:
		file.write(letter.encode("hex"))
		file.write(" ")
		if (i == 15):
			file.write("\n")
			i=0
		else:
			i+=1
	while (i != 0):
		file.write("00 ")
		if (i == 15):
			i=0
		else:
			i+=1
	hashFile.write(hashlib.md5(input).hexdigest())

userInput = raw_input("Enter text to encode: ")
try:
	encodeText(userInput)
	print "File written to: output"
	print "Hash written to: hash"
except:
	print "Error in encoding text. Exiting."
hashFile.close()
file.close()
raw_input("Press Enter to exit.")