#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(f'https://api.github.com/repos/{argv[2]}/{argv[1]}'
                     '/commits')
    if r.status_code == 200:
        for commit in r.json()[:10]:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
