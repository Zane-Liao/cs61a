#from ucb import trace 

def split(n):
    return n // 10, n % 10

def sum_split(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_split(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return lhun_sum_split(all_but_last) + last

def lhun_sum_split(n):
    all_but_last, last = split(n)
    lhun_digit = sum_split(2 * last)
    if n < 10:
        return lhun_digit
    else:
        return lhun_sum(all_but_last) + lhun_digit

# @trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)

# def grow(n):
#    if n // 10 != 0:
#        grow(n // 10)
#        print(n // 10)

# def shrink(n):
#    if n // 10 != 0:
#        print(n // 10)
#       shrink(n // 10)

def trace(f):
    def g(n, m):
        print(f.__name__ + '(' + str(n) + ',' + str(m) + ') was called')

        result = f(n, m)
        print(f.__name__ + '(' + str(n) + ',' + str(m) + ') -> ' + str(result))
        return result
    return g

@trace
def count_partitions(n, m):
    """Count the partitions of n using parts up to size m.

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(10, 10)
    42
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, min(m, n-m))
        without_m = count_partitions(n, m-1)
        return with_m + without_m


