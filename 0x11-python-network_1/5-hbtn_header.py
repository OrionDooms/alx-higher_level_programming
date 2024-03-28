#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id
"""

import requests
import sys


def html_request_x(url):
    response = requests.get(url)
    x = response.headers["X-Request-Id"]
    print(x)


if __name__ == "__main__":
    url = sys.argv[1]
    html_request_x(url)
