import os
from Crypto.Hash import SHA256
from pathlib import Path

#for hash file
if __name__ == "__main__":
    hash_file_path = Path("/home/cse/Lab3/Q2hash.txt")
    files_path = Path("/home/cse/Lab3/Q2files")


    with open(hash_file_path, 'rb') as file:
        hash_compare = file.read().strip()

    hash_compare = hash_compare.decode()
    hash_compare = bytes.fromhex(hash_compare) #convert hex to raw bytes


#exe Q2 files
    for exefile in files_path.iterdir():
        if exefile.is_file():
            with open(exefile, 'rb') as file:
                content = file.read()
                hasher = SHA256.new()
                hasher.update(content)
                hashed_content = hasher.digest()

                
                if hashed_content == hash_compare:
                    print(exefile.name)
                    break
                    

