#!/usr/bin/python3

def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i == "." or i == "?" or i == ":":
            print("\n\n", end="")
