import subprocess
from time import time
import sys
import hashlib

start = time()
login = "/home/cse/Lab1/Q6/Login.pyc"

with open("/home/cse/Lab1/Q6/PwnedPWs100k", "r") as f:
    passwords = f.read().splitlines()

with open("/home/cse/Lab1/Q6/gang", "r") as f:
    members = f.read().splitlines()

with open("/home/cse/Lab1/Q6/SaltedPWs", "r") as f:
    saltedpws = f.read().splitlines()

numbers = []
for i in range(10):
    numbers.append(str(i))

for line in passwords:
    line = line.strip()
    for j in saltedpws:
        j = j.strip().split(",")   
        for i in numbers:
            temppass = line + i
            saltedtemppass = j[1] + temppass
            h = hashlib.sha256()
            h.update(bytes(saltedtemppass, 'utf-8'))
            hashed_guess = h.hexdigest()
            if j[2] == hashed_guess:
                answer = subprocess.run(["python3", login, j[0], temppass], text = True, capture_output = True)
                if ("Login successful" in answer.stdout):
                    print(time() - start)
                    print(j[0])
                    print(temppass)
                    sys.exit(0)
    
                
print(time() - start)
sys.exit(1)
