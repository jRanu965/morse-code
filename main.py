# Morse Code Encryptor / Decryptor

def main():
    print("Morse Code Program Starting...")

main() 

# Morse Code Encryptor / Decryptor
# PSEUDOCODE:
# 1. Create Morse dictionary
# 2. Create reverse dictionary
# 3. Format input
# 4. Encrypt function
# 5. Decrypt function
# 6. Ask user for choice
# 7. Process input
# # 8. Display result

def main():
    print("Morse Code Program Starting...")

main() 

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    ' ': '/'
}

reverse_morse_dict = {value: key for key, value in morse_dict.items()}
def format_text(text):
    return text.strip().upper()

def encrypt(text):
    text = format_text(text)
    encrypted = ""

    for char in text:
        if char in morse_dict:
            encrypted += morse_dict[char] + " "
        else:
            encrypted += "? "

    return encrypted.strip()

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

def main():
    print("=== Morse Code Program ===")

    choice = input("Encrypt (E) or Decrypt (D)? ").strip().upper()

    if choice == 'E':
        message = input("Enter message: ")
        result = encrypt(message)
        print(result)

    elif choice == 'D':
        message = input("Enter Morse code: ")
        result = decrypt(message)
        print(result)

    else:
        print("Invalid choice.")
        
def main():
    print("==============================")
    print(" MORSE CODE ENCRYPTOR/DECODER ")
    print("==============================")

    choice = input("Encrypt (E) or Decrypt (D)? ").strip().upper()

    if choice == 'E':
        message = input("Enter message: ")
        result = encrypt(message)

        print("\nEncrypted Message:")
        print(result)

    elif choice == 'D':
        message = input("Enter Morse code: ")
        result = decrypt(message)

        print("\nDecrypted Message:")
        print(result)

    else:
        print("Invalid choice.") 

        if choice not in ['E', 'D']:
            print("Please enter only E or D.")
    return
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
reverse_morse_dict = {value: key for key, value in morse_dict.items()}
def format_text(text):
    return text.strip().upper()
