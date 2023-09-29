#!/usr/bin/python3
'''Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id'''
import requests
import sys


if __name__ == "__main__":
    owner = sys.argv[1]
    repo = sys.argv[2]
    para = {'per_page': 10}
    url = f'https://api.github.com/repos/{repo}/{owner}/commits?'
    resp = requests.get(url, params=para)

    if resp.status_code == 200:
        commit = resp.json()

        for com in commit:
            committer = com.get("commit").get("author").get("name")
            sha = com.get("sha")
            print("{}: {}".format(sha, committer))
