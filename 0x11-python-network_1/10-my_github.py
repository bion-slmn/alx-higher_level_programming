#!/usr/bin/python3
'''Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id'''
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    info = HTTPBasicAuth(user, passwd)
    url = 'https://api.github.com/user'

    r = requests.get(url, auth=info)
    print(r.json().get('id'))
