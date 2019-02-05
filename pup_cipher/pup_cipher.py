#! /usr/bin/python
# Written by ticarpi
# Decryption by ticarpi
# Algorithms built by trinity

import argparse
import urllib

##### Argparse #####
parser = argparse.ArgumentParser(description='Decrypt/Encrypt data with the 0A1Q1H1L1Gzu cipher')
parser.add_argument(dest='code', help='input code/plaintext to process')
parser.add_argument('-n', dest='nopretty', action='store_true', help='No pretty-print - doesn\'t add linebreaks and URL-decoding')
parser.add_argument('-e', dest='encrypt', action='store_true', help='Encrypt string')
args = parser.parse_args()

def decrypt(code):
	output = ""
	for i in range(0, len(code), 2):
		a, b = code[i], code[i+1]
		offset = 0
		if a == "t":
			offset = 0
		elif a == "y":
			offset = 0
		elif a == "z":
			offset = 56
		elif a == "0":
			offset = (2*ord(b)-ord(a))
		elif a == "1":
			offset = 132
		elif a == "2":
			offset = 156
		else:
			print "First char in pair does not match cipher scheme: %s" % a
			exit(0)
		output += chr(ord(a)-ord(b)+offset)
	return output

def pretty(output):
	pretty = ""
	for i in range(0,len(output)):
		cur = output[i]
		if cur == "&":
			pretty += "\n"
		else:
			pretty += cur
	return urllib.unquote(pretty)

def encrypt(code):
	output = ""
	for i in range(len(code)):
		x = ord(code[i])
		y = ""
		if x <= 51:
			y += "t"
			y += chr((ord(y) - x))
		elif x in range(52,56):
			y += "y"
			y += chr(ord(y) - x)
		elif x in range(56,65):
			y += "z"
			y += chr((ord(y) - (x - 56)))
		elif x in range(65,95):
			y += "0"
			y += chr(x)
		elif x in range(95,116):
			y += "1"
			y += chr((ord(y) - (x - 132)))
		elif x >= 116:
			y += "2"
			y += chr((ord(y) - (x - 156)))
		else:
			print "out of range"
			exit(0)
		output += y
	return output

print "============="
print "Cipher Output"
print "============="

def main():
	if args.encrypt == True:
		print encrypt(args.code)
	elif args.nopretty == True:
		print decrypt(args.code)
	else:
		print pretty(decrypt(args.code))

if __name__ == '__main__':
	main()
