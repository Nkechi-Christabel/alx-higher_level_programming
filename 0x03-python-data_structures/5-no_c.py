#!/usr/bin/env python3

def no_c(my_string):
    return (''.join([ch for ch in my_string if ch not in ('c', 'C')]))
