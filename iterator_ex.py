arr = [1,2,3]
arr_iter = iter(arr)
#arr_iter = arr.__iter__() # both are same
#print(arr_iter)
#print(next(arr_iter))
#print(next(arr_iter))
#print(next(arr_iter))
# when there is no more elements, it raises StopIteration execption.
#print(next(arr_iter))

while True:
    try:
        item = next(arr_iter)
        #print(item)
    except StopIteration:
        break

name = 'fahim'
name_iter = iter(name)
#print(name_iter)
#print(next(name_iter))
#print(next(name_iter))


class Yrange:
    def __init__(self,n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i +=1
            return i
        else:
            raise StopIteration()
a_range = Yrange(5)
# when two works both next or for loop it seems same
# because it runs after the current stage
#print(next(a_range))
#for i in a_range:
#    print(i)

# If both iteratable and iterator are the same object,
# it is consumed in a single iteration
#print(list(a_range))
#print(list(a_range))

class Zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return Zrange_iter(self.n)

class Zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

b_range = Zrange(5)
#print(list(b_range))
#print(list(b_range))

# Write an iterator class reverse_iter, 
# that takes a list and iterates it from 
# the reverse direction.
class Reverse_iter:
    def __init__(self, arr):
        self.arr = arr
        self.reverse_arr = self.arr[::-1]
        self.i = 0
        self.n = len(self.arr)
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.n :
            i = self.reverse_arr[self.i]
            self.i += 1
            return i
        else:
            raise StopIteration()

arr_reverse = Reverse_iter([1,2,3,4])
#print(next(arr_reverse))
#print(next(arr_reverse))
#print(next(arr_reverse))
#print(next(arr_reverse))
#print('----')
class Reverse_iter_other:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(self.arr)-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < 0 :
            n = self.arr[self.n]
            self.n -= 1
            return n
        else:
            raise StopIteration()

arr_reverse_other = Reverse_iter([1,2,3,4])
#print(next(arr_reverse_other))
#print(next(arr_reverse_other))
#print(next(arr_reverse_other))
#print(next(arr_reverse_other))

import itertools
it1 = iter([1,2,3])
it2 = iter([4,5,6])
#print(list(itertools.chain(it1,it2)))

#for x,y in itertools.zip_longest(['a','b','c'],[1,2,3]):
#    print(x,y)

# Write a function peep, that takes an iterator as argument 
# and returns the first element and an equivalant iterator. 
def peep(iterator):
    return next(iterator), iterator

x,it = peep(iter(range(5)))
#print(x)
#print(it)
#print(list(it))

# The built-in function enumerate takes an iteratable 
# and returns an iterator over pairs (index, value) 
# for each value in the source.
def my_enumerate(arr):
    i=0
    for element in arr:
        yield (i,element)
        i +=1
print(my_enumerate(['a','b','c']))
print(list(my_enumerate(['a','b','c'])))
for i,c in my_enumerate(['a','b','c']):
    print(i,c)

# Implement a function izip that works like itertools.izip.
def izip(list1, list2):
    return ((list1[i],list2[j]) for i in range(len(list1)) \
        for j in range(len(list2)) if i==j) 
print(izip(['a','b','c'],[1,2,3]))
print(list(izip(['a','b','c'],[1,2,3])))

