#!/bin/bash
#Bash script takes in a URL, sends a POST request and displays it.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
