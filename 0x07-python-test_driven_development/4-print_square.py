#!/usr/bin/python3
# Print square


def print_square(size):
    """defines a function print_square that takes the param size.
    size is the size length of the square
    size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    print(((size * '#') + '\n') * size)
