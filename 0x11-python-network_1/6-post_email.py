#!/usr/bin/python3
"""
A script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the body.
"""

import requests
import sys


def html_POST_request(url, email):
    email_value = {'email': email}
    url_data = requests.post(url, email_value)
    print(url_data.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    html_POST_request(url, email)
