from math import pi,sqrt

def area(r, shape_constant):
    assert r > 0, 'A length must be positive'
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)

def lib(n):
    x, y = 1, 0
    k = 0
    while k < n:
        x, y = y, x + y
        k = k + 1
    return y

# print('-------------------------------------------------------------')

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.
    
    >>> summation(5, cube)
    225

    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    """
    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)

def sum_cubes(n):
    """
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)

def make_adder(n):
    """
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def is_three(x):
    return x == 3

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

def inverce(f):
    def inverce_sqrt(y):
        def inverce_square(x):
            return f(x) == y
        return search(inverce_square)
    return inverce_sqrt
#    return lambda y: search(lambda x: f(x) == y)

def if_(c ,t, v):
    if c:
        return t
    else:
        return v

# def real_sqrt(x):
#    if x > 0:
#        return sqrt(x)
#   else:
#        return 0.0

def real_sqrt(x):
    return if_(x > 0, sqrt(x), 0.0)

def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10

def reasonable(n):
    return n == 0 or 1/n != 0
