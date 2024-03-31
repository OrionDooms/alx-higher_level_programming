#!/bin/bash
#A Bash script that takes in a URL, sends a GET request and displays the body
curl -so /dev/null -w "%{http_code}" $1
