import doctest
import functools


def prod(xs):
    """Multiply a list of numbers
    >>> prod([1, 2, 3])
    6
    """
    return functools.reduce(lambda a, b: a * b, xs)


class Memoize:
    def __init__(self, f):
        self.f = f
        self.m = {}

    def __call__(self, *args):
        if args not in self.m:
            self.m[args] = self.f(*args)
        return self.m[args]

if __name__ == "__main__":
    doctest.testmod()
