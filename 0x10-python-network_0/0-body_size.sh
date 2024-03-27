#!/bin/bash
#A bash script that takes in a URL, sends a request to that URL
#and displays the size of the body.
URL="$1"
curl -s $URL | wc -c
