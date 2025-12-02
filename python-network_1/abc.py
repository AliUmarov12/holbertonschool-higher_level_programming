#!/usr/bin/python3
"""ekljdkrjdirj"""

import urllib.request

if __name__ == "__main__":
    url = https://intranet.hbtn.io/status

    with urllib.request.urlopen(url) as abc:
        a = abc.read()
        print('Body response:')
        print('\t- type: {}'.format(type(a)))
        print('\t- content: {}'.format(a))
        print('\t- utf8 content: {}'.format(a.decode("utf-8")))

