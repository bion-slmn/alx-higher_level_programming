#!/usr/bin/python3
'''Python script that takes in a URL and an email,
    sends a POST request to the passed URL'''
import sys
from urllib.request import urlopen
from urllib import parse, request

if __name__ == "__main__":
    email_add = sys.argv[2]
    url = sys.argv[1]
    value = {'email': email_add}
    data = parse.urlencode(value).encode('ascii')

    req = request.Request(url, data)
    with urlopen(req) as r:
        print(r.read().decode('utf-8'))
