#!/usr/bin/python3
'''Python script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id '''
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen(sys.argv[1]) as r:
        print(r.headers['X-Request-Id'])
