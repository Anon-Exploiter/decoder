#!/usr/bin/python3

from codecs import encode
import argparse
from sys import path
path.append("./dependencies/")
from encd import *
from banner import *
from termcolor import colored

"""
Supported Encodings (for now -- add a request through issues!)
 - base16
 - base32
 - base64
 - base85
 - atbash
 - baconian
 - caesar
 - morse
 - rot13
 - rot47
"""

def addArguments():
	# -------------------------------------------------\n\tStrings Decoder\n-------------------------------------------------\n\n
	parser = argparse.ArgumentParser(description='', usage=f'\r[#] Usage: python3 decoder.py --file file.txt')
	parser._optionals.title = "Basic Help"

	opts = parser.add_argument_group(f'Arguments')
	opts.add_argument('-s', '--string', 	action="store", 	dest="string", 		default=False, 		help='String to decode!')
	opts.add_argument('-f', '--file', 		action="store", 	dest="file", 		default=False, 		help='File to decode!')

	args = parser.parse_args()
	return(args, parser)

def getFileContents(file):
	with open(file, 'r') as f: return( f.read().strip() )

def main():
	args, parser = addArguments()

	if args.file:
		string = args.file
		string = getFileContents(string)

	elif args.string:
		string = args.string

	else:
		parser.print_help()
		exit()

	print("---")
	print(f"[{colored('#', 'cyan')}] Provided string: {colored(string, 'green')}")
	print("---")
	print()

	if ("Exception" not in base16Decode(string)):
		devider()
		basetitle()
		print(f"[{colored('+', 'green')}] Base16 decoded: {colored(base16Decode(string), 'green')}")
	elif ("Exception" not in base32Decode(string)):
		devider()
		basetitle()
		print(f"[{colored('+', 'green')}] Base32 decoded: {colored(base32Decode(string), 'green')}")
	elif ("Exception" not in base64Decode(string)):
		devider()
		basetitle()
		print(f"[{colored('+', 'green')}] Base64 decoded: {colored(base64Decode(string), 'green')}")
	elif ("Exception" not in base85Decode(string)):
		devider()
		basetitle()
		print(f"[{colored('+', 'green')}] Base85 decoded: {colored(base85Decode(string), 'green')}")

	devider()
	commonEncodingTitle()

	print(f"[{colored('+', 'green')}] AtBash decoded: {colored(atbashDecode(string), 'green')}")
	if ("Exception" not in baconianDecode(string)):
		print(f"[{colored('+', 'green')}] Baconian decoded: {colored(baconianDecode(string), 'green')}")
	if (morseDecode(string) != " "):
		print(f"[{colored('+', 'green')}] Morse decoded: {colored(morseDecode(string), 'green')}")
	devider()

	rotTitle()
	print(f"[{colored('+', 'green')}] ROT13 decoded: {colored(rot13Decode(string), 'green')}")
	print(f"[{colored('+', 'green')}] ROT47 decoded: {colored(rot47Decode(string), 'green')}")
	devider()

	ceasertitle()

	for shift in range(0, 10):
		print(f"[{colored('&', 'green')}] Shift: {shift} Decoded: {colored(cipherDecrypt(string, shift), 'green')}")
	devider()
	print()

if __name__ == '__main__':
	banner()
	main()