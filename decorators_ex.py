def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
#print(fib(3))

def trace(f):
    def g(x):
        print(f.__name__, x)
        value = f(x)
        print('return', repr(value))
        return value
    return g
#fib = trace(fib)
#print(fib(3))

def trace_readable(f):
    f.indent = 0
    def g(x):
        print('| ' * f.indent + '|--',f.__name__,x)
        f.indent +=1
        value = f(x)
        print('| ' * f.indent + '|--','return',repr(value))
        f.indent -=1
        return value
    return g
#fib = trace_readable(fib)
#print(fib(4))

@trace_readable 
# It is equivalant of adding 
# fib = trace(fib) after the function definition
def fib_check(n):
    if n == 0 or n==1:
        return 1
    else:
        return fib(n-1)+ fib(n-2)
#fib_check(4)

def memorize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g
#fib = trace_readable(fib)
#fib = memorize(fib)
#print(fib(4))

# Write a function profile, which takes a function 
# as argument and returns a new function, which 
# behaves exactly similar to the given function, 
# except that it prints the time consumed in executing it.
def profile(f):
    from datetime import datetime
    start = datetime.now().microsecond
    def g(x): 
        value = f(x)
        return value
    end = datetime.now().microsecond
    print(end-start)
    return g
#fib = profile(fib)
#print(fib(30))

# Write a function vectorize which takes a function f 
# and return a new function, which takes a list as argument 
# and calls f for every element and returns the result as a list.
def vectorize(f):
    def g(x):
        lst = []
        for element in x:
            lst.append(f(element))
        return lst
    return g     
def square(x): return x*x
f = vectorize(square)
print(f([1,2,3]))
g = vectorize(len)
print(g(['hello','world']))
print(g([[1,2],[4,3,5]]))
    
