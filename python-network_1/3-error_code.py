#!/usr/bin/python3
"""dklhfjrhfvur"""

import urllib.request
import urllib.error
import sys

if _name_ == "_main_":
    url = sys.argv[1]

    request = urllib.request.Request(url, headers={'cfclearance': 'true'})

    try:
        with urllib.request.urlopen(request) as f:
            r = f.read()
            print(r.decode("utf-8"))

    except urllib.error.HTTPError as g:
        print("Error code: ", g.code)
