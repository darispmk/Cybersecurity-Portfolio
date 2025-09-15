from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

# Hardcoded Private Key
private_key = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCMqf4MyQYxZ5wxuYbFtztnRdeY4mVfgzFUs2/9i4nUJvlltSdD
7NApUynU+5UeyLo+kUpxpWSvFc2H+3RDHrNVqxDsDKqeoh2giLPQP1bh+oiBQM3e
EQiEOHC+OW3fFNIe47EB4j0sEtK+vlrR0BGqIwHOgabaFqJATO+K+QSJ8wIDAQAB
AoGACaCa5DogA+KhBKA7kq2zUaKsmmioYoyipDbxy8swoEYYnLb03IfJSYLJIqwj
bSt039Jm43db+EXIPu3da7iesnzWxTjg7TGp7SnqpUoxDDK5YwtppMwJ7imWRae7
O/iQl5VSJ6TqsLCKLScpK/zVuZli4RM6mqb8ihl99mX61AECQQC2DoZ3C8vmCP6X
4P1iEGsqlEw5Ul9/EKlpgkLjsiwh+W4o6IgO/YUc/Efph5rqQYc2k6dKeysV7o+g
8bJzmbXzAkEAxcuhyamMeRH9EP6zbTGNoDx5eI+2+enNpu1iMbKy0UFpFGb/XxYg
K3cc83RhKOPUjmdzB9GLPdDgwP2m/DrcAQJAXOhavMP7YUBz1MRP6sygNBGMOLCN
5YV2P07nndWeahQloKDSVnwQg3NHq6i1aRjZzQNbG0px+XZOO/88Z3wo+wJBAIyd
cpxKI+piZnWxjN9g7h1vQK/8A4nxtFkqw7cvIj7vcIOnoX743M/pszRElVobdh3y
3208g+/jUhUBfrgsJAECQGen1/b33n45h3mv7GKCDm9mIOQ2BSv1yPh1X0dPpjjR
s+unpawHxTZA8NiB60++Qnx7NYPNe5FEy8m0DX+bpVc=
-----END RSA PRIVATE KEY-----"""


file = input()
attacking_directory = "/home/cse/Lab3/" + file

# Import the Private Key
rsa_key = RSA.import_key(private_key)
cipher_rsa = PKCS1_OAEP.new(rsa_key)

# Loop Through Files in the Target Directory
for file in os.listdir(attacking_directory):
    filepath = os.path.join(attacking_directory, file)

    # Decrypt Only .txt Files
    if filepath.endswith(".txt"):
        with open(filepath, "rb") as f:
            encrypted_data = f.read()

        # Decrypt Data in Chunks
        chunk_size = 128  # Max size for RSA decryption
        decrypted_chunks = [cipher_rsa.decrypt(encrypted_data[i:i+chunk_size]) for i in range(0, len(encrypted_data), chunk_size)]

        # Write the Decrypted Data to the Same File
        with open(filepath, "wb") as f:
            for chunk in decrypted_chunks:
                f.write(chunk)

