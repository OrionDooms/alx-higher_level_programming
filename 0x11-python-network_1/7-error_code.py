#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body.
If the HTTP status code is greater than or equal to 400, print: Error code.
"""

import requests
import sys


def html_Error_status(url):
    result = requests.get(url)
    if result.status_code >= 400:
        print("Error code: {}".format(result.status_code))
    else:
        print(result.text)


if __name__ == "__main__":
    url = sys.argv[1]
    html_Error_status(url)
