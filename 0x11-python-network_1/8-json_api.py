#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response using requests package.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1].isdigit():
        print("No result")
        sys.exit()

    q = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    j = r.json()
    print(f"[{j['id']}] {j['name']}" if j else "Not a valid JSON")
