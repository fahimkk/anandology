a = [5,9,7]
b = [1,2,3]
c = [x+y for x,y in zip(a,b)]
#print(c)

# pythagorian triplet
n = 25
x = [(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x*x + y*y == z*z]
#print(x)

# Provide an implementation for zip function using list comprehensions.
aa = ['a','b','c']
bb = [1,2,3]
cc = [(bb[i],aa[j]) for i in range(len(aa)) for j in range(len(bb)) if i==j]
#print(cc)

# Python provides a built-in function map that applies a function 
# to each element of a list. 
# Provide an implementation for map using list comprehensions.
def square(x): return x*x
k = map(square,range(5))
#print(list(k))

kk = [square(x) for x in range(5)]
#print(kk)

# Python provides a built-in function filter(f, a) that 
# returns items of the list a for which f(item) returns true. 
# Provide an implementation for filter using list comprehensions
def even(x):  return x%2 == 0
f = filter(even,range(10))
#print(list(f))

ff = [x for x in range(10) if even(x)]
#print(ff)

# Write a function triplets that takes a number n as argument and 
# returns a list of triplets such that sum of first two elements of 
# the triplet equals the third element using numbers below n. 
# Please note that (a, b, c) and (b, a, c) represent same triplet
def triplets(n):
    triplet_list = []
    for i in range(1,n):
        for j in range(i,n):
            if i+j < 5:
                triplet_list.append((i,j,i+j))
    return triplet_list
#print(triplets(5))

# Write a function array to create an 2-dimensional array. 
# The function should take both dimensions as arguments. 
# Value of each element can be initialized to None:
def array(m,n): # m dimension, n elements
    return [[None]*n]*m
print(array(2,3))


