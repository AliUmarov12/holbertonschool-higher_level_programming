#!/usr/bin/python3
"""nbnvjbjh"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    res = requests.post(url, data=data)
    try:
        json_data = res.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit(0)
    if not json_data:
        print("No result")
    else:
        print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
