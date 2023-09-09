#!/usr/bin/env python3

def no_c(my_string):
    return ([ch for ch in my_string if ch not in ('c', 'C')].join(''))
