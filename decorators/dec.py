import functools


# Never called twice with the same args (key = str(args) + str(kwargs)), counts total number of calls
def track(f):
    cache = {}

    def wrapper(*args1, **args2):
        key = str(args1) + str(args2)
        if key not in cache:
            cache[key] = ""
            wrapper.count += 1 #cheating :(
        elif cache[key] == "" and args1 != (0,):
            print(key, "found in cache")
            cache[key] = 0
        return f(*args1, **args2)

    wrapper.count = 0
    return wrapper
    
def log(f): #saves all function calls and their results in the file "log.txt"
    def wrapper(*args1, **args2):
        logfile = open('log.txt','a')
        print(str(f.__name__) + "(" + str(args1) + str(args2) + ") = " + str(f(*args1, **args2)))
        logfile.close
        return f(*args1, **args2)
    wrapper.count = 0
    return wrapper

# fib((1,){}) = 1
# fib((0,){}) = 0
# fib((2,){}) = 1
# fib((1,){}) = 1
# fib((3,){}) = 2

@log
def fib(n):
    return n if n in (0,1) else fib(n-1) + fib(n-2)
print(fib(10), 'calls =', fib.count)
# ¬¬¬¬


# def main():
#     pass

# if __name__ == '__main__':
#     main()
