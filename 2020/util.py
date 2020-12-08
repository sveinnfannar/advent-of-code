import doctest
import functools


def prod(xs):
    """Multiply a list of numbers
    >>> prod([1, 2, 3])
    6
    """
    return functools.reduce(lambda a, b: a * b, xs)


if __name__ == "__main__":
    doctest.testmod()
