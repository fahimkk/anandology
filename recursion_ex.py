def exp(x,n):
    """ Computes the result of x raised to
    the power of n.
        exp(2,3) = 8
        exp(3,2) = 9 """
    if n == 0 :
        return 1
    else:
        return x * exp(x,n-1)
#print(exp(3,4))

def fast_exp(x,n):
    if n==0:
        return 1
    elif n % 2 == 0:
        return fast_exp(x*x, n//2)
    else:
        return x * fast_exp(x, n-1)
#print(fast_exp(3,4))

# Implement a function product to multiply 2 numbers 
# recursively using + and - operators only.
def product(x,n):
    if n ==1:
        return x
    else:
        return x + product(x,n-1)
#print(product(7,8))

# Supposed you have a nested list and 
# want to flatten it.
def flatten_list(arr, result=None):
    """ Flattens a nested list.
        flatten_list([[1,2,[3,4]],[5,6],7])
        [1,2,3,4,5,6,7] """
    if result is None:
        result = []
    for x in arr:
        if isinstance(x,list):
            flatten_list(x,result)
        else:
            result.append(x)
    return result
#print(flatten_list([[1,2,[3,4]],[5,6],7]))

# Write a function flatten_dict to flatten a nested 
# dictionary by joining the keys with . character.
def flatten_dict(dictionary,result=None, parant=None):
    """flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
        {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}"""
    if result is None:
        result = {}
    for key,value in dictionary.items():
        if isinstance(value,dict):
            if parant is None:
                parant = key
            else:
                parant = f'{parant}.{key}'
            flatten_dict(value,result,parant)
            parant = None
        else:
            if parant is None:
                result[key] = value
            else:
                result[f'{parant}.{key}'] = value
    return result
#print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))
#print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': {'a':8}}, 'c': 4}))

# Write a function unflatten_dict to do reverse of flatten_dict.
def unflatten_dict_norecursion(dictionary):
    result_dict = {}
    for key, value in dictionary.items():
        parts = key.split('.')
        d = result_dict
        for part in parts[:-1]:
            if part not in d:
                d[part] = {}
            d = d[part]
        d[parts[-1]] = value
    return result_dict
#print(unflatten_dict_norecursion({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))


# Write a function tree_reverse to reverse 
# elements of a nested-list recursively.
def tree_reverse(arr):
    """tree_reverse([[1, 2], [3, [4, 5]], 6])
        [6, [[5, 4], 3], [2, 1]]"""
    for element in arr:
        if isinstance(element,list):
            tree_reverse(element)
            element.reverse()
    return arr[::-1]

def tree_reverse_outer(arr):
    """tree_reverse([[1, 2], [3, [4, 5]], 6])
        [6, [[5, 4], 3], [2, 1]]"""
    import copy
    result = copy.deepcopy(arr)
    def tree_reverse_inner(result):
        for element in result:
            if isinstance(element,list):
                tree_reverse_inner(element)
                element.reverse()
        return result
    result = tree_reverse_inner(result)
    result.reverse()
    return result

s = [[1, 2], [3, [4, 5]], 6]
#print(tree_reverse([[1, 2], [3, [4, 5]], 6]))
#print(tree_reverse_outer(s))
#print(tree_reverse(s))
#print(s)


# Write a function treemap to map a function over nested list.
def square(x):
    return x*x

def treemap(func, arr):
    """ treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
        [1, 4, [9, 16, [25]]]"""
    for index, element in enumerate(arr):
        if isinstance(element,list):
            treemap(func,element)
        else:
            arr[index] = func(element)
    return arr  

#print(treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]))
#print(treemap(square,s))

# Implement a program dirtree.py that takes a directory as argument 
# and prints all the files in that directory recursively as a tree.
def dirtree(directory,indent=None):
    import os
    filenames = os.listdir(directory)
    if indent is None: 
        indent = 1
    for filename in filenames:
        filepath = os.path.join(directory,filename)
        if os.path.isdir(filepath):
            print('| '+'|--'*indent,filename)
            indent+=1
            dirtree(filepath,indent)
            indent-=1
        else:
            print(f'| {"|--"*indent}{filename}') 

#dirtree('/home/fahim/tutorial/automateTheBoringStuff/pdffiles')

