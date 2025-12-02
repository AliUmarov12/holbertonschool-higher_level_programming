#!/usr/bin/python3
"""dklhfjrhfvur"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(url) as f:
            print(f.read().decode("utf-8"))

    except urllib.error.HTTPError as g:
        print("Error code: ", g.code)
