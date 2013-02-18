# spacedHexDecoder
# By David Gedarovich <dave.gedarovich@gmail.com>
# Takes in a space-seperated hex file and an accompanying hash file to decode
# and check against each other for data consistency. Files are deleted upon use.

import hashlib
import os
file = open("output", "r")
try:
	hashFile = open("hash", "r")
	hashIn = hashFile.readline().strip()
	hashExists = True
except:
	hashIn = hashlib.md5("0").hexdigest()
	print "WARNING: No hash file found, data integrity cannot be confirmed!"
	hashExists = False
textIn = file.readlines()

def decodeText(text, hash):
	fullText = ""
	for line in text:
		lineDecode = line.replace(" ", "").strip()
		print line.strip() + " = " + lineDecode.decode("hex")
		fullText += lineDecode.decode("hex")
	fullText = fullText.rstrip('\0')
	print "Full text: " + fullText
	if (hashExists):
		print "Encoded Hash: " + hash
		print "Decoded Hash: " + hashlib.md5(fullText).hexdigest()
		if (hash == hashlib.md5(fullText).hexdigest()):
			print "Hash match - data secure!"
		else:
			print "WARNING: Hash mismatch - data insecure!"

try:
	decodeText(textIn, hashIn)
except:
	print "Error in decoding text. Exiting."
if (hashExists):
	hashFile.close()
	os.remove("hash")
file.close()
os.remove("output")
raw_input("Press Enter to exit.")
