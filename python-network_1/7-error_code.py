#!/usr/bin/python3
"""dkfnkrnvijfvnjr"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    try:
        print(req.text)
    except requests.error.HTTPError as g:
        if g.code >= 400:
            print("Error code:", g.code)
