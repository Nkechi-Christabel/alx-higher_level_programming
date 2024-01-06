#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
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
