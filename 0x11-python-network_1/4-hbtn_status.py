#!/usr/bin/python3
"""A Python script that fetches the content of a website and display it.
"""


import requests


def html_fetches(url):
    html = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print('\t- content: {}'.format(html.text))


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    html_fetches(url)
