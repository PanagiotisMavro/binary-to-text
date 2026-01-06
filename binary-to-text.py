import argparse

# Function to convert binary to text
def binary_to_text(binary_str, encoding='utf-8'):
    binary_values = binary_str.replace(" ", "").replace(",", "").replace("\t", "").replace("\n", "")

    if len(binary_values) % 8 != 0:
        raise ValueError("Binary string length must be a multiple of 8")

    text = ''.join(chr(int(binary_values[i:i+8], 2))
                   for i in range(0, len(binary_values), 8))

    return text.encode(encoding).decode(encoding)


# ---------------------- Banner ----------------------
def print_banner():
    print(r"""
 ____  _                              _              _            _   
| __ )(_)_ __   __ _ _ __ _   _      | |_ ___       | |_ _____  _| |_ 
|  _ \| | '_ \ / _` | '__| | | |_____| __/ _ \ _____| __/ _ \ \/ / __|
| |_) | | | | | (_| | |  | |_| |_____| || (_) |_____| ||  __/>  <| |_ 
|____/|_|_| |_|\__,_|_|   \__, |      \__\___/       \__\___/_/\_\\__|
                          |___/                                       
""")


def main():
    print_banner()   # 👈 THIS WAS MISSING

    parser = argparse.ArgumentParser(description="Binary to Text Converter")

    parser.add_argument('-t', '--text', type=str,
                        help="Text to convert to binary")
    parser.add_argument('-d', '--binary', type=str,
                        help="Binary string to convert to text")
    parser.add_argument('-e', '--encoding', type=str,
                        default='utf-8',
                        help="Character encoding (default: utf-8)")

    args = parser.parse_args()

    if args.text:
        binary_str = ' '.join(format(ord(c), '08b') for c in args.text)
        print(f"\nBinary of '{args.text}':\n{binary_str}")

    elif args.binary:
        try:
            text = binary_to_text(args.binary, encoding=args.encoding)
            print(f"\nConverted Text:\n{text}")
        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("\nError: You must provide either --text or --binary")


if __name__ == "__main__":
    main()
