# Binary to Text Converter

A Python script to convert **binary strings to text** and **text to binary**, supporting various delimiters and custom encoding.

## Features
- Convert **text to binary**.
- Convert **binary to text**.
- Support for **custom delimiters** (e.g., space, comma).
- **Character encoding** support (default is `utf-8`, but you can use `utf-16` or others).

## If Problem for pip? Can help you (Working) Kali Linux
- sudo apt install python3-venv
- python3 -m venv ~/myenv
- source ~/myenv/bin/activate

## Installation

You don’t need to install anything to use this script. Just clone the repository and run the script.

## LINUX OR ARCH LINUX
KALI,UBUNTU,DEBIAN AND OTHER TO LINUX 

```bash
git clone https://github.com/PanagiotisMavro/binary-to-text
cd binary-to-text-converter

1. Convert Text to Binary
- python3 binary-to-text.py -t "hello world!"
Example:
- Binary of 'hello world!': 01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100 00100001
Example with Custom Encoding (utf-16):
- python3 binary-to-text.py -d "01001000 01100101 01101100 01101100 01101111" -e utf-16
