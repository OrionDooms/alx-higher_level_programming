#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id
"""

import urllib.request
import sys


def html_request(url):

    with urllib.request.urlopen(url) as response:
        request = response.headers.get('X-Request-Id')
        print(request)


if __name__ == "__main__":
    url = sys.argv[1]
    html_request(url)
