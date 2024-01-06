#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response using requests package.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.text if r.status_code < 400 else f'Error code: {r.status_code}')
