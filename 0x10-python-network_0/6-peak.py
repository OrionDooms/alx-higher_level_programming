#!/usr/bin/python3
#A algorithm that finds a peak in a list of unsorted integers
def find_peak(list_of_integers):
    if not list_of_integers:
        temp = None
    else:
        temp = 0
    for i in range(len(list_of_integers)):
        if list_of_integers[i] > temp:
            temp = list_of_integers[i]
    return temp
