#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) < 0:
        sentence = None
    else:
        s = len(sentence)
        return (s, sentence[:1])
