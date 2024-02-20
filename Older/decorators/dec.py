
def track(f):
    cache = {}
    def wrapper(*args1, **args2):
        key = str(args1) + str(args2)
        if key not in cache:
            wrapper.count += 1
            result = f(*args1, **args2)
            cache[key] = result
        else:
            print(key, "found in cache")
        return cache[key]
    wrapper.count = 0
    return wrapper
    
def log(f):
    def wrapper(*args1, **args2):
        result = f(*args1, **args2)
        with open('decorators\log.txt','a') as logfile:
            logfile.write(f.__name__ + "(" + str(args1) + str(args2) + ") = " + str(result) + "\n")
            logfile.close
        return result
    return wrapper

@track
@log
def fib(n):
   return n if n in (0,1) else fib(n-1) + fib(n-2)
print(fib(10), 'calls =', fib.count) # No comma unless I change this to str() :(
