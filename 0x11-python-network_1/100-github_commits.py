#!/usr/bin/python3
'''Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id'''
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    value = {"Accept": "application/vnd.github+json"}
    url = f' https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits'
    r = requests.get(url, headers=value)

    for r_dic in r.json():
        print(f"{r_dic.get('sha')}: {r_dic['commit']['author']['name']}")
