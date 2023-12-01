#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= 0:
        for i in range(len(my_list)):
            if idx < i:
                return ('none')
            elif idx == i:
                return (my_list[i])
    else:
        return ('none')
