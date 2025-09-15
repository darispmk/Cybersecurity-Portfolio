from Crypto.Hash import SHA256 
from Crypto.Signature import pkcs1_15 
from Crypto.PublicKey import RSA
import os

def main(): 
    key = RSA.import_key(open("/home/cse/Lab3/Q3pk.pem", 'rb').read()) 
    for exe in os.listdir("/home/cse/Lab3/Q3files"): 
        if exe.endswith(".exe"): 
            file_path = f"/home/cse/Lab3/Q3files/{exe}" 
            sig_path = f"/home/cse/Lab3/Q3files/{exe}.sign" 
            try: 
                with open(file_path, 'rb') as f:
                    content = f.read() 
                with open(sig_path, 'rb') as f:
                    sig = f.read() 

                hash_obj = SHA256.new(content) 
                pkcs1_15.new(key).verify(hash_obj, sig) 
                print(exe) 
                break 
            except Exception: 
                continue 

if __name__ == "__main__": 
    main() 
