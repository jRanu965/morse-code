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