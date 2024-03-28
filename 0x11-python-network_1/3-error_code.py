#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body.
Manage urllib.error.HTTPError exceptions and print: Error code.
"""

import urllib.request
import sys


def html_Error_code(url):
    try:
        with urllib.request.urlopen(url) as response:
            result = response.read().decode('utf-8')
            print(result)
    except urllib.error.HTTPError as e:
        error = e.code
        print("Error code: {}".format(error))


if __name__ == "__main__":
    url = sys.argv[1]
    html_Error_code(url)
