#!/usr/bin/env python3

def no_c(my_string):
    new_str = [ch for ch in my_string if ch not in ('c', 'C')]
    return (''.join(new_str))
