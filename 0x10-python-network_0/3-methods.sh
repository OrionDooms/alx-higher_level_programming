#!/bin/bash
#A Bash script takes in a URL and displays all HTTP methods the server
curl -siX OPTIONS $1 | grep -i "allow:" | cut -d ':' -f 2
