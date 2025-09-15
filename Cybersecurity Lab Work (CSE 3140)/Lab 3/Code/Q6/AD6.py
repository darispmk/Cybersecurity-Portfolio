from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from base64 import b64encode

private_key = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCbFSDwEHCzc5mD4R9qnXgaG4fGK/jRQADoHKNtooZ/6+A+4QrS
s7e/jPU6VkDF6w/3PEIUd4oWLohevODwTzjlDiK0ANDpMubVLBvHvOai/yOs8NPZ
VuQRxfHR5dxCTG9ILOMilisvQ2KExVdMT/CKNU626A0rDBlfHwzkScytrwIDAQAB
AoGAQlzZwfD/EUOkC0OwKnLlHKLwSHSznnN5j9oFc1prnN0GklHBzGVceYsru0GC
qU8L/3vZOSHoRNK3x3ai+SKlkPAENg4Ei1eZ47wqK8v1rZVVlVaLNiVJIczXOYoi
0UtZMuScaGqRl+uBVx9Tt50tqIxDqGiSszRkHq1EFstRu7UCQQC2/K95JDJcD2QH
EYh0veoasL/VKJ4Lh/5loEC7ZMrNGXp2v068+8pc91UbvdFJiPdAyWhC5b4ePMva
wH9aLwu1AkEA2PYe3097rCjsUUy4XkSmaEiZ3ZF5aINZgUo88vHdafYRWrLSqEeo
SzT9cPyqSbpuFPcvtQEf/p0ecXaLPB2aUwJADVzyq5QbIWH2WhXLs0rTN9PEjpqC
wDDUQTOsxoKb1NKRgO6Dn4V7x8JAMuBv0kDwXYjX1lrUwXyLHpSEOF/LKQJBAI8p
0PNP8m6GznFTK7FgoWHczlMLRE63pZ8PyqoQ+SaLbaYoq6LJLf76Z2ZgA0oFT9Bb
z8ojhOYw7T63l2bCresCQBgd1r50f5hbfhhjCf+h+GHiz6OadWz2nXuuepsLD0Pk
bO8JbcWjUgdxaJsXqb0AESgcUTct3qwIfah7eRIHG3k=
-----END RSA PRIVATE KEY-----"""

encrypted_shared = input()
encrypted_shared_key = f"/home/cse/Lab3/Solutions/Q6/EncryptedFolder/{encrypted_shared}"

decrypted_shared_key_file = "/home/cse/Lab3/Solutions/Q6/DecryptedSharedKey"

with(open(encrypted_shared_key,"rb")) as c:
    all_lines = c.read()


rsa_key = RSA.import_key(private_key)
cipher_rsa = PKCS1_OAEP.new(rsa_key)
decrypted_message = cipher_rsa.decrypt(all_lines)


with(open(decrypted_shared_key_file,"w")) as f:
    f.write(str(decrypted_message))
