from Crypto.PublicKey import RSA

if __name__ == "__main__":
    #step 1 generate keypair e and d
    key = RSA.generate(1024)
    D_private_key = key.export_key()
    E_public_key = key.publickey().export_key()

    D_private_file = "/home/cse/Lab3/Solutions/Q6/d.key.pem"
    E_public_file = "/home/cse/Lab3/Solutions/Q6/e.key.pem"


    with (open(D_private_file, "wb")) as f:
        f.write(D_private_key)

    with (open(E_public_file, "wb")) as f:
        f.write(E_public_key)


