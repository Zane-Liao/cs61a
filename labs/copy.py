def count(s, value):
    """
    >>> count([1, 2, 2, 2, 3], 2)
    3
    """
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

def count_same(pairs):
    """Return how many pairs have the same element repeated.

    >>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
    >>> count_same(pairs)
    2
    """
    same_count = 0
    for x, y in pairs:
        if x == y:
            same_count = same_count + 1
    return same_count

def mysum(L):
    if (L==[]):
        return 0
    else:
        return L[0] + mysum(L[1:])

def mysum_iter(L):
    total = 0
    if (L==[]):
        return 0
    else:
        for x in L[0:]:
            total += x
    return total

def count_for(n):
    sum = 0
    if n == 0:
        return 0
    else:
        for i in range(0, n + 1):
            sum += i
    return sum

def count(n):
    if n == 0:
        return 0
    else:
        return n + count(n - 1)

def divisors(n):
    return [1] + [x for x in range(2, n) if n%x==0]

def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
