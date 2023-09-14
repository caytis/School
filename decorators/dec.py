import functools




# Never called twice with the same args (key = str(args) + str(kwargs)), counts total number of calls
def track(f):
    def wrapper(*args1, **args2):
        key = {}
        wrapper.count += 1
        if args1 in key:
            pass
        else:
            key = str(args1) + str(args2)
            print(key, "found in cache")
            return f(*args1, **args2)
    wrapper.count = 0
    return wrapper

    # (1,){} found in cache
    # (2,){} found in cache
    # (3,){} found in cache
    # (4,){} found in cache
    # (5,){} found in cache
    # (6,){} found in cache
    # (7,){} found in cache
    # (8,){} found in cache

@track
def fib(n):
    return n if n in (0,1) else fib(n-1) + fib(n-2)

def main():
    print(fib(10), 'calls =', fib.count)
    # ¬¬¬¬
    pass


if __name__ == '__main__':
    main()
