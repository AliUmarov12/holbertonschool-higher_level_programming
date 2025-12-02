#!/usr/bin/python3
"""dklhfjrhfvur"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    request = urllib.request.Request(url, headers={'cfclearance': 'true'})

    try:
        with urllib.request.urlopen(url) as f:
            r = f.read()
            print(r.decode("utf-8"))

    except urllib.error.HTTPError as g:
        print("Error code: ", g.code)
