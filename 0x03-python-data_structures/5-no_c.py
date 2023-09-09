#!/usr/bin/env python3

def no_c(my_string):
    filtered_str = ''
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            filtered_str += ch
    
    return (filtered_str)
