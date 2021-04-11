import base64
import pycipher
from codecs import encode

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
