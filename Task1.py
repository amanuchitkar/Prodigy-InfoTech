def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust the shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            # Handle lowercase letters
            elif char.islower():
                new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result += new_char
        else:
            result += char  # Non-alphabet characters stay the same
    
    return result

if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypt the message
    encrypted_message = caesar_cipher(message, shift, mode='encrypt')
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = caesar_cipher(encrypted_message, shift, mode='decrypt')
    print(f"Decrypted message: {decrypted_message}")
