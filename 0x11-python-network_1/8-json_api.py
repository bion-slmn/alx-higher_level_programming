#!/usr/bin/python3
'''Python script that takes in a letter and sends a POST
 request to http:/0.0.0.0:5000/search_user '''
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    value = {'q': letter}

    resp = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        r = resp.json()
        if not r:
            print('No result')
        else:
            print(f"[{r.get('id')}] {r.get('name')}")
    except Exception as e:
        print('Not a valid JSON')
