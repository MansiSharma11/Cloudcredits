# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# import binascii

# # Padding functions to ensure data is a multiple of 16 bytes (block size for AES)
# def pad(data):
#     padding_length = 16 - (len(data) % 16)
#     return data + bytes([padding_length]) * padding_length

# def unpad(data):
#     return data[:-data[-1]]

# # Encryption function
# def encrypt(card_number, key):
#     cipher = AES.new(key, AES.MODE_ECB)  # Using ECB mode (use a more secure mode in practice)
#     padded_card_number = pad(card_number.encode('utf-8'))
#     encrypted = cipher.encrypt(padded_card_number)
#     return binascii.hexlify(encrypted).decode('utf-8')

# # Decryption function
# def decrypt(encrypted_card_number, key):
#     cipher = AES.new(key, AES.MODE_ECB)
#     encrypted_card_number_bytes = binascii.unhexlify(encrypted_card_number.encode('utf-8'))
#     decrypted = unpad(cipher.decrypt(encrypted_card_number_bytes))
#     return decrypted.decode('utf-8')

# # Example usage
# key = get_random_bytes(16)  # AES-128 requires a 16-byte key

# credit_card_number = input('Enter a credit card number: ')

# encrypted_card_number = encrypt(credit_card_number, key)
# print('Encoded number =', encrypted_card_number)

# decrypted_card_number = decrypt(encrypted_card_number, key)
# print('Decoded number =', decrypted_card_number)


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii
import re

# Padding functions to ensure data is a multiple of 16 bytes (block size for AES)
def pad(data):
    padding_length = 16 - (len(data) % 16)
    return data + bytes([padding_length]) * padding_length

def unpad(data):
    return data[:-data[-1]]

# Encryption function
def encrypt(card_number, key):
    iv = get_random_bytes(16)  # Generate a random initialization vector (IV)
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Using CBC mode for more security
    padded_card_number = pad(card_number.encode('utf-8'))
    encrypted = cipher.encrypt(padded_card_number)
    return binascii.hexlify(iv + encrypted).decode('utf-8')  # Prepend IV to encrypted data for use in decryption

# Decryption function
def decrypt(encrypted_card_number, key):
    encrypted_card_number_bytes = binascii.unhexlify(encrypted_card_number.encode('utf-8'))
    iv = encrypted_card_number_bytes[:16]  # Extract the IV (first 16 bytes)
    encrypted_data = encrypted_card_number_bytes[16:]  # The rest is the encrypted data

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_data))
    return decrypted.decode('utf-8')

# Validate card number (simple check to ensure it's numeric and a valid length)
def validate_card_number(card_number):
    if not re.match(r'^\d{16}$', card_number):
        raise ValueError("Invalid credit card number. It must be 16 digits.")
    return card_number

# Main function to execute the encryption and decryption
def main():
    key = get_random_bytes(16)  # AES-128 requires a 16-byte key

    credit_card_number = input('Enter a 16-digit credit card number: ')
    
    try:
        # Validate the card number
        card_number = validate_card_number(credit_card_number)
        
        # Encrypt the card number
        encrypted_card_number = encrypt(card_number, key)
        print('Encrypted card number:', encrypted_card_number)

        # Decrypt the card number
        decrypted_card_number = decrypt(encrypted_card_number, key)
        print('Decrypted card number:', decrypted_card_number)

    except ValueError as e:
        print(e)

# Run the program
if __name__ == "__main__":
    main()
