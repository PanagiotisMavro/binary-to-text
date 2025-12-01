import argparse

# Function to convert binary to text
def binary_to_text(binary_str, encoding='utf-8'):
    # Clean up the binary string (remove delimiters)
    binary_values = binary_str.replace(" ", "").replace(",", "").replace("\t", "").replace("\n", "")
    
    # Ensure the binary is in 8-bit chunks
    if len(binary_values) % 8 != 0:
        raise ValueError("Binary string length must be a multiple of 8")
    
    # Convert each byte (8 bits) into a character
    text = ''.join(chr(int(binary_values[i:i+8], 2)) for i in range(0, len(binary_values), 8))
    
    # Return the decoded text
    return text.encode(encoding).decode(encoding)

# Function to handle the command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Binary to Text Converter")
    
    # Optional: Text input flag
    parser.add_argument('-t', '--text', type=str, help="Text to convert to binary (optional)", default=None)
    
    # Optional: Binary input flag
    parser.add_argument('-d', '--binary', type=str, help="Binary string to convert to text (optional)", default=None)
    
    # Optional: Specify encoding
    parser.add_argument('-e', '--encoding', type=str, help="Character encoding (default: utf-8)", default='utf-8')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Convert text to binary
    if args.text:
        # Convert text to binary
        binary_str = ' '.join(format(ord(c), '08b') for c in args.text)
        print(f"Binary of '{args.text}': {binary_str}")
    
    # Convert binary to text
    elif args.binary:
        try:
            text = binary_to_text(args.binary, encoding=args.encoding)
            print(f"Converted Text: {text}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Error: You must provide either a text or binary string.")

if __name__ == "__main__":
    main()
