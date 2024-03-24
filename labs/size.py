def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)
    
def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

def count_frames(f):
        def counted(n):
            counted.open_count += 1
            counted.max_count = max(counted.max_count, counted.open_count)
            result = f(n)
            counted.open_count -= 1
            return result
        counted.open_count = 0
        counted.max_count = 0
        return counted

def memo(f):
    cache = {}
    def memorixed(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorixed