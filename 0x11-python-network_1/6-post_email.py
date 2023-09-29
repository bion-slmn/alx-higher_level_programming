#!/usr/bin/python3
'''Python script that takes in a URL and an email,
    sends a POST request to the passed URL'''
import sys
import requests


if __name__ == "__main__":
    email_add = sys.argv[2]
    url = sys.argv[1]
    value = {'email': email_add}

    resp = requests.post(url, data=value)
    print(resp.text)
