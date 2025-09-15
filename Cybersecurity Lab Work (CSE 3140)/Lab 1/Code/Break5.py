import subprocess
from time import time
import sys
import hashlib

start = time()
login = "/home/cse/Lab1/Q5/Login.pyc"

with open("/home/cse/Lab1/Q5/PwnedPWs100k", "r") as f:
    passwords = f.read().splitlines()

with open("/home/cse/Lab1/Q5/gang", "r") as f:
    members = f.read().splitlines()

with open("/home/cse/Lab1/Q5/HashedPWs", "r") as f:
    hashedpass = f.read().splitlines()

numbers = []
for i in range(10):
    for j in range(10):
        numbers.append(str(i) + str(j))

for line in passwords:
    line = line.strip()
    for j in hashedpass:
        j = j.strip().split(",")
        for i in numbers:
            temppass = line + i
            h = hashlib.sha256()
            h.update(bytes(temppass, 'utf-8'))
            hashed_guess = h.hexdigest()
            if (j[1] == hashed_guess):
                answer = subprocess.run(["python3", login, j[0], temppass], text = True, capture_output = True)
                if ("Login successful.\n" == answer.stdout):
                    print(j[0])
                    print(temppass)
                    print(time() - start)
                    sys.exit(0)

print(time() - start)
sys.exit(1)
