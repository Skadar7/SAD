from functools import wraps

memo = {}
PERF = {}


def make_perf():
    def count(func):
        def exec(n):
            name = func.__name__
            if (name not in PERF.keys()):
                PERF[name] = 1
            else:
                PERF[name] += 1
            return func(n)

        return exec

    return count


perf = make_perf()


def memoize(function):
    @wraps(function)
    def wrapper(*args):
        if args not in memo:
            memo[args] = function(*args)

        return memo[args]

    return wrapper


@memoize
@perf
def fib(n):
    if (n < 2): return n
    return (fib(n - 1) + fib(n - 2))


@perf
def fib2(n):
    if (n < 2): return n
    return (fib2(n - 1) + fib2(n - 2))


fib(20)
fib2(20)

print(PERF)