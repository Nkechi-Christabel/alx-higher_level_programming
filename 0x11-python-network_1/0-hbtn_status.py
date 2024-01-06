#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
                                as response:
        html = response.read()
        decoded_html = html.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", decoded_html)
