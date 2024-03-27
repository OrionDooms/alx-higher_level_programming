#!/bin/bash
#A bash script takes in a URL, sends a request and displays the size
curl -s $1 | wc -c
