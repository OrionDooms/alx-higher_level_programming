#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id
"""

import urllib.request
import sys


def html_POST(url, email):

    email_value = {'email': email}
    data = urllib.parse.urlencode(email_value)
    data = data.encode('utf-8')
    url_data = urllib.request.Request(url, data)
    with urllib.request.urlopen(url_data) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    html_POST(url, email)
