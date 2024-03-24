from operator import floordiv, mod, mul

def divide_exact(n, d=10):
    """

    >>> r, f, b = divide_exact(2013, 10)
    >>> r
    201
    >>> f
    3
    >>> b
    20130

    """
    return floordiv(n, d) , mod(n, d), mul(n, d)

def absolute_value(x):
    """
    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(2)
    2
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else: 
        return x

def prime_factors(n):
    """
    >>> prime_factors(6)
    2
    3
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallet_factors(n) 
        n = n // k
        print(k)

def smallet_factors(n):
    k = 2
    while n % k != 0:
        k = k + 1
    return k

    # while n > 1:
    #   k = 2
    #   while n % k != 0:
    #       k = k + 1
    #   n = n // k
    #   print(k)
