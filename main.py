# Morse Code Encryptor / Decryptor

def main():
    print("Morse Code Program Starting...") 

main() 
# 1. Morse dictionary 
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/'
}

# 2. Reverse dictionary
reverse_morse_dict = {value: key for key, value in morse_dict.items()}

# 3. Format input
def format_text(text):
    return text.strip().upper()

# 4. Encrypt function
def encrypt(text):
    text = format_text(text)
    encrypted = ""

    for char in text:
        if char in morse_dict:
            encrypted += morse_dict[char] + " "
        else:
            encrypted += "? "

    return encrypted.strip()

# 5. Decrypt function
def decrypt(morse_code):
    morse_code = morse_code.strip()
    symbols = morse_code.split(" ")

    decrypted = ""

    for symbol in symbols:
        if symbol in reverse_morse_dict:
            decrypted += reverse_morse_dict[symbol]
        else:
            decrypted += "?"

    return decrypted

# 6. Main program
def main():
    print("==============================")
    print(" MORSE CODE ENCRYPTOR/DECODER ")
    print("==============================")

    while True:
        choice = input("\nEncrypt (E), Decrypt (D), or Quit (Q)? ").strip().upper()

        if choice == 'E':
            message = input("Enter message: ")
            print("\nEncrypted Message:")
            print(encrypt(message))

        elif choice == 'D':
            message = input("Enter Morse code: ")
            print("\nDecrypted Message:")
            print(decrypt(message))

        elif choice == 'Q':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter E, D, or Q.")

# 7. Run program
if __name__ == "__main__":
    main()
