#!/usr/bin/python3
"""
Sends a request to a URL and prints the response body (utf-8 decoded).
Handles HTTPError by printing: Error code: <status>
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print(body.decode("utf-8"))

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
