#!/usr/bin/python3
'''  Python script that fetches https://alx-intranet.hbtn.io/status
using python urllib'''
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        response = r.read()
        print('Body response:')
        print(f'\t- type: {type(response)}')
        print(f'\t- content: {response}')
        print(f"\t- utf8 content: {response.decode('utf-8')}")
