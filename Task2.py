from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, output_path, key):
    """
    Encrypts an image by adding the key to each pixel's RGB value.
    This is a simple form of encryption that modifies pixel values.
    
    :param image_path: The path of the image to encrypt
    :param output_path: The path to save the encrypted image (must include file name and extension)
    :param key: An integer key used for encryption
    """
    # Open the image
    img = Image.open(image_path)
    # Convert image to a NumPy array
    img_array = np.array(img)
    
    # Add the key to each pixel value and ensure it wraps around at 255
    encrypted_array = (img_array + key) % 256
    
    # Convert back to an image and save the encrypted image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    """
    Decrypts an image by subtracting the key from each pixel's RGB value.
    This reverses the encryption process by using the same key.
    
    :param image_path: The path of the encrypted image
    :param output_path: The path to save the decrypted image (must include file name and extension)
    :param key: An integer key used for encryption and decryption
    """
    # Open the encrypted image
    img = Image.open(image_path)
    # Convert image to a NumPy array
    img_array = np.array(img)
    
    # Subtract the key from each pixel value and ensure it wraps around at 255
    decrypted_array = (img_array - key) % 256
    
    # Convert back to an image and save the decrypted image
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    print("Image Encryption Tool")
    action = input("Do you want to (e)ncrypt or (d)ecrypt an image? ")
    
    if action.lower() == 'e':
        image_path = input("Enter the path of the image to encrypt: ").strip()
        output_path = input("Enter the path to save the encrypted image (include file name and extension): ").strip()
        key = int(input("Enter the encryption key (integer): "))
        
        if not os.path.splitext(output_path)[1]:
            print("Error: The output path must include a file name and extension (e.g., encrypted_image.jpg).")
        else:
            encrypt_image(image_path, output_path, key)
        
    elif action.lower() == 'd':
        image_path = input("Enter the path of the encrypted image: ").strip()
        output_path = input("Enter the path to save the decrypted image (include file name and extension): ").strip()
        key = int(input("Enter the decryption key (integer): "))
        
        if not os.path.splitext(output_path)[1]:
            print("Error: The output path must include a file name and extension (e.g., decrypted_image.jpg).")
        else:
            decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice! Please choose (e)ncrypt or (d)ecrypt.")
