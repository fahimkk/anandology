
# Write a function valuesort to sort values of a dictionary based on the key.
# returns a list of values sorted based on keys
a = {'x': 1, 'y': 2, 'a': 3}
def valuesort(dictionary):
    value_list = []
    sorted_key = sorted(a.keys())
    for key in sorted_key:
        value_list.append(dictionary[key])
    return value_list
#print(valuesort(a))

# Write a function invertdict to interchange keys and values in a dictionary. 
# For simplicity, assume that all values are unique.
def invertdict(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    return new_dict
print(invertdict(a))

# Write a program to find anagrams in a given list of words. 
# Two words are called anagrams if one word can be formed by rearranging 
# letters of another. For example 'eat', 'ate' and 'tea' are anagrams.
def anagrams(arr):
    anagrams_list = []
    visited = set()
    for i in range(len(arr)):
        if arr[i] not in visited:
            element_list = [arr[i]]
            for j in range(i+1,len(arr)):
                if arr[j] not in visited and sorted(arr[i]) == sorted(arr[j]) :
                    element_list.append(arr[j])
                    visited.add(arr[j])
            visited.add(arr[i])
            anagrams_list.append(element_list)
    return anagrams_list
#print(anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']))

def anagrams_without_sort(arr):
    anagrams_list = []
    freq_dict = {}
    # create a dictionary with key as the item and 
    # value is dictionary with character frequecy
    for element in arr:
        if element not in freq_dict:
            freq_dict[element] ={}
            for char in element:
                freq_dict[element][char]= freq_dict[element].get(char,0) + 1
    visited=set()
    # check the character frequecy.
    for element in freq_dict.keys():
        if element not in visited:
            element_list = [element]
            visited.add(element)
            for key, value in freq_dict.items():
                if key not in visited and freq_dict[element] == value:
                    visited.add(key)
                    element_list.append(key)
            anagrams_list.append(element_list)
    return anagrams_list 
print(anagrams_without_sort(['eat', 'ate', 'done', 'tea', 'soup', 'node']))

def f(a,b):print(locals())
f(1,2)