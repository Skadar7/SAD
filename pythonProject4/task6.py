PERF = {}

def make_perf():
    def count(func):
        def exec(n):
            name = func.__name__
            if (name not in PERF.keys()): PERF[name] = 1
            else: PERF[name] += 1
            return func(n)
        return exec
    return count


perf = make_perf()

@perf
def fact(n):
    if (n < 2): return 1
    else: return n*fact(n-1)


@perf
def fib(n):
    if (n == 0): return 0
    elif ((n == 1) or (n == 2)): return 1
    else: return (fib(n-1) + fib(n-2))


fact(10)
fib(27)
print(PERF)