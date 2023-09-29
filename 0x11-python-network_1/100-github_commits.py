#!/usr/bin/python3
'''Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id'''
import requests
import sys


if __name__ == "__main__":
    url = f' https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits'
    r = requests.get(url)

    for count, r_dic in enumerate(r.json()):
        committer = r_dic.get('commit').get('author').get('name')
        sha = r_dic.get('sha')
        print(f"{sha}: {committer}")
        if count == 9:
            break
