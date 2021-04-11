# Decoder
> Automating the Manual :)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub](https://img.shields.io/github/license/Anon-Exploiter/decoder)
[![Contributors][contributors-shield]][contributors-url]
![GitHub closed issues](https://img.shields.io/github/issues-closed/Anon-Exploiter/decoder)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=%40syed_umar)](https://twitter.com/syed__umar)

[contributors-shield]: https://img.shields.io/github/contributors/Anon-Exploiter/decoder.svg?style=flat-square
[contributors-url]: https://github.com/Anon-Exploiter/decoder/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/Anon-Exploiter/decoder.svg?style=flat-square
[issues-url]: https://github.com/Anon-Exploiter/decoder/issues

![image](https://user-images.githubusercontent.com/18597330/114285294-9a8e5a80-9a6f-11eb-9475-d251c0ea522a.png)

A simple script to try and decode a string in various encoding mechanisms regardless of it's (original) type. 

The one-liner doesn't make much sense right? Don't worry, I gotcha! 

Let's say you've a string _(you obtained from somewhere, maybe a boot2root machine, ctf, etc.)_, you know it's encoded _(isn't a hash and is not encrypted)_ but just can't figure out the encoding mechanism used? No worries, this script will try and decode it in most used encoding mechanisms (i.e. base64, rot47, atbash, etc.) 

Once the results come back, make sure to go through each and every line! That's all manual :3 

The script for now only supports: 

- Base16
- Base32
- Base64
- Base85
- Atbash
- Baconian
- Caesar
- Morse
- Rot13
- Rot47

### Tested On (OS & Python version)
- Ubuntu 20.04 LTS -- Python 3.8.5
- Arch Linux -- Python 3.9.2

### Downloading
```csharp
git clone https://github.com/Anon-Exploiter/decoder/
cd decoder/
```

### Usage

Decoding a string from directly from argument:
```bash
python3 decode.py -s 'uryyb'
```

Decoding a string from a file:
```bash
python3 decode.py -f rot47-encoded.txt
```

### Todos
- <s>Add colors</s>
- Utilize internal libraries to add all the decoding (rather than custom written code)

### Filing Bugs/Contribution
Feel free to file a issue or create a PR for that issue if you come across any.

### Screenshots
![image](https://user-images.githubusercontent.com/18597330/114285317-beea3700-9a6f-11eb-9352-a276b4a8d510.png)

![image](https://user-images.githubusercontent.com/18597330/114285322-c3165480-9a6f-11eb-9ac1-0834adcc4487.png)

![image](https://user-images.githubusercontent.com/18597330/114285324-c578ae80-9a6f-11eb-9eef-85cd0fc11ea8.png)

![image](./ScreenShots/decoder_ss.png)

### Credits
- Big thanks to [autodecoder](https://github.com/oreosES/autodecoder) (was a lot of help while writing this)
- Thanks to [@thehackersbrain](https://twitter.com/thehackersbrain)'s [Blogger](https://www.vulnhub.com/series/blogger,462/) machine which made me write this

#### Well this is shit work, any other tools which have the same functionality and actually work? Yes!
- https://github.com/oreosES/autodecoder
- https://github.com/Ciphey/Ciphey
