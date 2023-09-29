#!/usr/bin/python3
'''Python script that takes in a URL, sends a request to the
    URL and displays the body of the response '''
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print(f'Error code: {r.status_code}')
