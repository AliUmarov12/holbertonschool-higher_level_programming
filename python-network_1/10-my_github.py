#!/usr/bin/python3
"""kldjvivi"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    abc = requests.get(url, auth=(username, password))
    try:
        abcd = abc.json()
        print(abcd.get("id"))
    except:
        print(None)
