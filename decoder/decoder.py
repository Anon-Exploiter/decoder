#!/usr/bin/python3

from termcolor import colored
from codecs import encode

import argparse
import base64
import pycipher

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

def banner():
	title = """________                          .___            
\\______ \\   ____   ____  ____   __| _/___________ 
 |    |  \\_/ __ \\_/ ___\\/  _ \\ / __ |/ __ \\_  __ \\
 |    `   \\  ___/\\  \\__(  <_> ) /_/ \\  ___/|  | \\/
/_______  /\\___  >\\___  >____/\\____ |\\___  >__|   
        \\/     \\/     \\/           \\/    \\/       

              Automate the Manual :)
"""
	
	print(colored(title, "green"))

def basetitle():
	print(f"[{colored('%', 'yellow')}] Base Encodings (16 - 85)")

def ceasertitle():
	print(f"[{colored('%', 'yellow')}] Ceaser Cipher (with shifts 0 - 9)")

def commonEncodingTitle():
	print(f"[{colored('%', 'yellow')}] Common Encodings")

def rotTitle():
	print()
	print(f"[{colored('%', 'yellow')}] Rot Encodings (13 - 47)")
	print()

def divider():
	print("-------------------------------------------------------")

def base16Decode(string):
	try:
		return base64.b16decode(string).decode()

	except Exception as e:
		return f"Exception: {e}"

def base32Decode(string):
	try:
		return base64.b32decode(string).decode()

	except Exception as e:
		return f"Exception: {e}"

def base64Decode(string):
	try:
		return base64.b64decode(string).decode()

	except Exception as e:
		return f"Exception: {e}"

def base85Decode(string):
	try:
		return base64.b85decode(string).decode()

	except Exception as e:
		return f"Exception: {e}"

def atbashDecode(string):
	try:
		return pycipher.Atbash().decipher(string)
	
	except Exception as e:
		return f"Exception: {e}"

def baconianDecode(string):
	try:
		lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
			'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
			'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
			'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
			'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}

		decipher = ''
		i = 0

		string = string.lower()
	  
		while True:
			if(i < len(string)-4):
				substr = string[i:i + 5]

				if(substr[0] != ' '):
					decipher += list(lookup.keys())[list(lookup.values()).index(substr)]
					i += 5 
	  
				else:
					decipher += ' '
					i += 1

			else:
				break
	  
		return decipher

	except Exception as e:
		return f"Exception: {e}"

def cipherDecrypt(string, key):
	decrypted = ""

	for c in string:
		if c.isupper(): 
			c_index = ord(c) - ord('A')
			c_og_pos = (c_index - key) % 26 + ord('A')
			c_og = chr(c_og_pos)
			decrypted += c_og

		elif c.islower(): 
			c_index = ord(c) - ord('a') 
			c_og_pos = (c_index - key) % 26 + ord('a')
			c_og = chr(c_og_pos)
			decrypted += c_og

		elif c.isdigit():
			c_og = (int(c) - key) % 10
			decrypted += str(c_og)

		else:
			decrypted += c

	return decrypted

def morseDecode(string):
	dictionary =  {
		'.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
		'...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R',
		'.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
		'.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
		'.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
		'---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
		'....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
		'-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
		'--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':',
		'-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
		'----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'
	}

	translated = []

	for item in string.split(' '):
		if dictionary.get(item) != None:
			translated.append(dictionary.get(item))

		else:
			translated.append(' ')

	translated = ''.join(translated).rstrip('\n')
	return(translated)

def rot13Decode(string):
	return encode(string, 'rot13').rstrip('\n')

def rot47Decode(string):
	try:
		x = []
		for i in range(len(string)):
			j = ord(string[i])
			if j >= 33 and j <= 126:
				x.append(chr(33 + ((j + 14) % 94)))
			else:
				x.append(string[i])
		return ''.join(x)

	except Exception as e:
		return f"Exception: {e}"

def main():
	banner()

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
		divider()
		print()
		basetitle()
		print(f"[{colored('+', 'green')}] Base16 decoded: {colored(base16Decode(string), 'green')}")

	elif ("Exception" not in base32Decode(string)):
		divider()
		print()
		basetitle()
		print(f"[{colored('+', 'green')}] Base32 decoded: {colored(base32Decode(string), 'green')}")

	elif ("Exception" not in base64Decode(string)):
		divider()
		print()
		basetitle()
		print(f"[{colored('+', 'green')}] Base64 decoded: {colored(base64Decode(string), 'green')}")

	elif ("Exception" not in base85Decode(string)):
		divider()
		print()
		basetitle()
		print(f"[{colored('+', 'green')}] Base85 decoded: {colored(base85Decode(string), 'green')}")

	divider()
	print()
	commonEncodingTitle()

	print(f"[{colored('+', 'green')}] AtBash decoded: {colored(atbashDecode(string), 'green')}")

	if ("Exception" not in baconianDecode(string)):
		print(f"[{colored('+', 'green')}] Baconian decoded: {colored(baconianDecode(string), 'green')}")

	if (morseDecode(string) != " "):
		print(f"[{colored('+', 'green')}] Morse decoded: {colored(morseDecode(string), 'green')}")

	print()
	divider()

	rotTitle()
	print(f"[{colored('+', 'green')}] ROT13 decoded: {colored(rot13Decode(string), 'green')}")
	print(f"[{colored('+', 'green')}] ROT47 decoded: {colored(rot47Decode(string), 'green')}")
	print()

	divider()
	print()
	ceasertitle()
	print()

	for shift in range(0, 10):
		print(f"[{colored('&', 'green')}] Shift: {shift} Decoded: {colored(cipherDecrypt(string, shift), 'green')}")
	print()
	divider()

if __name__ == '__main__':
	main()