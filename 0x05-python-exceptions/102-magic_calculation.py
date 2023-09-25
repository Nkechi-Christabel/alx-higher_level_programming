#!/usr/bin/python3

def magic_calculation(a, b):
    """
    Performs a magic calculation based on the provided arguments.

    Args:
        a: An integer.
        b: An integer.

    Returns:
        The result of the calculation, which may vary based on conditions:
        - If 'i' exceeds 'a', an exception is raised with a message 'Too far',
          and the result becomes 'b + a'.
        - Otherwise, it calculates (a ** b) / i for 'i' in the range [1, 2, 3]
          and accumulates the results.
    """
    result = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception as e:
            result = b + a
            break
    return result
