#!/usr/bin/python3
'''Python script that takes in a URL, sends a request to the
    URL and displays the body of the response '''
import urllib
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
