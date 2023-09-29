#!/usr/bin/python3
'''Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id'''
import requests
import sys


if __name__ == "__main__":
    url = f' https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits'
    r = requests.get(url)
    com = r.json()

    for i in range(10):
        try:
            committer = com[i].get("commit").get("author").get("name")
            sha = com[i].get("sha")
            print("{}: {}".format(sha, committer))
        except IndexError:
            break
