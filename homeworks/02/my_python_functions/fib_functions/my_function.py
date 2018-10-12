def cache_decorator(func):
    mem_cache = {}
    
    def fnc(arg):
        if arg in mem_cache:
            return mem_cache[arg]
        else:
            mem_cache[arg] = func(arg)
            return mem_cache[arg]
    return fnc

@cache_decorator
def fib(n):
    if n<3:
        return 1
    return fib(n-1) + fib(n-2)