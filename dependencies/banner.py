from termcolor import colored

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
	print()
	print(f"[{colored('%', 'yellow')}] Base Encodings (16 - 85)")
	print()

def ceasertitle():
	print()
	print(f"[{colored('%', 'yellow')}] Ceaser Cipher (with shifts 0 - 9)")
	print()

def commonEncodingTitle():
	print()
	print(f"[{colored('%', 'yellow')}] Common Encodings")
	print()

def rotTitle():
	print()
	print(f"[{colored('%', 'yellow')}] Rot Encodings (13 - 47)")
	print()

def devider():
	print("-------------------------------------------------------")
