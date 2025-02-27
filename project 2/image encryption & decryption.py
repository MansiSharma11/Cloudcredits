from cryptography.fernet import Fernet
import os

class Encryption:
    def __init__(self, key):
        self.key = key

    def encrypt_data(self, data):
        if isinstance(data, bytes):
            pass
        else:
            data = data.encode()

        f = Fernet(self.key)

        cipher = f.encrypt(data)
        return cipher

    def decrypt_data(self, data):
        f = Fernet(self.key)
        return f.decrypt(data)

try:
    os.mkdir('encImages')
except:
    pass

try:
    os.mkdir('decImages')
except:
    pass

path = './Images/'
path2 = './encImages/'
path3 = './decImages/'
folder_images = os.listdir(path)
enc_images = os.listdir(path2)

key = None

def gen_key():
    key = Fernet.generate_key()
    with open('key.pem', 'wb') as f:
        f.write(key)
    
def encrypt_images():
    gen_key()
    for img in folder_images:
        with open(path+img,'rb') as f:
            data = f.read()

        with open('key.pem', 'rb') as f:
            key = f.read()

        enc = Encryption(key)

        enc_data = enc.encrypt_data(data)

        with open(path2+img,'wb') as f:
            f.write(enc_data)
    
    print('Done Encryption')

def decrypt_images():
    for img in enc_images:
        with open(path2+img, 'rb') as f:
            data = f.read()

        with open('key.pem', 'rb') as f:
            key = f.read()

        enc = Encryption(key)
        org_data = enc.decrypt_data(data)

        with open(path3+img, 'wb') as f:
            f.write(org_data)
    print('Done Decryption')

ch = input('Enter e for encryption and d for decryption: ')

if ch == 'e':
    encrypt_images()
elif ch == 'd':
    decrypt_images()
else:
    print('Invalid Input !!!')

