import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


if __name__ == "__main__":

    with open(os.path.join("/home/cse/Lab3/Q4files", "Encrypted4"), 'rb') as f:

        iv = f.read(16)
        key = b'\xc8\xa0:\xd4.\x1d\xff\x8f4\xaf\x01\xd6\xc6f\x12\x16' 
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)

        #read in encrypted file
        ciphertext = f.read(16)
    
        decrypted_data = cipher.decrypt(ciphertext)
        plaintext = unpad(decrypted_data, AES.block_size)

        print (plaintext)

