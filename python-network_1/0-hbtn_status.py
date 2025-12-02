#!/usr/bin/python3
"""dlmfkmkv"""

import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    a = urllib.request.Request(url, headers={'cfclearance': 'true'})

    with urllib.request.urlopen(url) as f:
        s = f.read()

    print("Body response:")
    print("    - type: {}".format(type(s)))
    print("    - content: {}".format(s))
    print("    - utf8 content: {}".format(s.decode("utf-8")))
