#!/usr/bin/python3
'''Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id'''
import requests
import sys


if __name__ == "__main__":
    url = f' https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits'
    resp = requests.get(url)

    if resp.status_code == 200:
        commit = resp.json()

        for com in commit[:10]:
            committer = com.get("commit").get("author").get("name")
            sha = com.get("sha")
            print("{}: {}".format(sha, committer))
