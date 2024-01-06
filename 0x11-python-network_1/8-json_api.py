#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response using requests package.
"""
import requests
import sys

if __name__ == "__main__":
    q = "" if len(sys.argv) != 2 else sys.argv[1]

    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        data = response.json()
        print(f"[{data['id']}] {data['name']}" if data else "No result")
    except ValueError:
        print("Not a valid JSON")
