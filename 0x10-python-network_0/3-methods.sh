#!/bin/bash
#A Bash script takes in a URL and displays all HTTP methods the server
curl -s -X OPTIONS -i $1 | grep "Allow" | cut -d " " -f 2-
