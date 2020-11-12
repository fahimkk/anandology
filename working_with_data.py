
# Zip
names = ['a','b','c']
values = [1,2,3]
#print(zip(names,values)) # will print zip object
for name, value in zip(names,values):
    #print(name,value)
    pass

# sum of list of string.
def sum_string(arr):
    text = ''
    for element in arr:
        text+= element
    return text
#print(sum_string(['hello ','world','!!']))

# product of a list of numbers
def product(arr):
    result = 1
    for num in arr:
        result = result * num
    return result
#print(product([2,3,5]))

# factorial of a num
def factorial(n):
    fact = 1
    for num in range(1,n+1):
        fact = fact * num
    return fact
#print(factorial(4))

# reverse of a list using slicing
def reverse_slicing(arr):
    return arr[::-1]
#print(reverse_slicing([1,2,3,4]))

# reverse of a list without using slicing
def reverse(arr):
    reverse_list=[]
    for i in range(len(arr)-1,-1,-1):
        reverse_list.append(arr[i])
    return reverse_list
#print(reverse([1,2,3,4]))

def cumulative_sum(arr):
    cum_sum_list = [arr[0]]
    for i in range(1,len(arr)):
        cum_sum_list.append(arr[i]+cum_sum_list[i-1])
    return cum_sum_list
#print(cumulative_sum([1,2,3,4]))

def cumulative_product(arr):
    cum_product_list = [arr[0]]
    for i in range(1,len(arr)):
        cum_product_list.append(arr[i]*cum_product_list[i-1])
    return cum_product_list
#print(cumulative_product([1,2,3,4]))

# to find all unique elements of a list
def unique(arr):
    # set only add elements once, 
    # we can avoid checking for each element
    unique_set = set()
    for element in arr:
        unique_set.add(element) 
    return list(unique_set)
#print(unique([1,2,3,1,5,2,3]))
#print(list(set([1,2,3,1,5,2,3])))

# to find all duplicates
def dups(arr):
    dups_list = []
    dups_set = set()
    for element in arr:
        if element not in dups_set:
            dups_set.add(element)
        else: dups_list.append(element)
    return dups_list
#print(dups([1,2,3,1,5,2,3]))

# Write a function group(list, size) that take a list 
# and splits into smaller lists of given size.
def group(arr, size):
    nested_list=[]
    start = 0
    for end in range(size,len(arr),size):
        nested_list.append(arr[start:end])
        start = end
    if start != len(arr):
        nested_list.append(arr[start:])
    return nested_list  
#print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

# Write a function lensort to sort a list of 
# strings based on length.
def lensort(arr):
    return sorted(arr, key=lambda x: len(x))
#print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))

# Improve the unique function written in previous problems 
# to take an optional key function as argument and use 
# the return value of the key function to check for uniqueness.

def unique_upadted(arr,key=lambda x: x):
    unique_set = set()
    for element in arr:
        unique_set.add(key(element)) 
    return list(unique_set)
#print(unique_upadted(["python", "java", "Python", "Java"], key=lambda s: s.lower()))

# Write a function extsort to sort a list of files based on extension.
def extsort(arr):
    return sorted(arr,key=lambda x: x.split('.')[1])
#print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c','y.txr']))

#Write a program to print each line of a file in reverse order.
def reverse_txt(filename):
    f = open(filename,'r')
    w = open(f'reverse_{filename}','w')
    # this doesn't work if the last line doesn'nt has new line 
    #w.writelines(f.readlines()[::-1])
    f_list = f.readlines()
    if not f_list[-1].endswith('\n'):
        f_list[-1] = f_list[-1]+'\n'
    w.writelines(f_list[::-1])
    f.close()
    w.close()
#reverse_txt('she.txt')