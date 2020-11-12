# Write a function count_change to count the number of ways to change any 
# given amount. Available coins are also passed as argument to the function.
# by recursion method
# n = amount, m = len(arr), ie to choose the element by index 
def count_change(n,arr,m=None):
    """ count_change(10, [1, 5]) = 3
        count_change(10, [1, 2]) = 6 """
    if m is None:
        m = len(arr)
    if n == 0:
        return 1 
    if n < 0:
        return 0
    if m<=0 and n>=1:
        return 0
    return count_change(n,arr,m-1) + count_change(n-arr[m-1],arr,m)
print(count_change(100, [1, 5,10,25,50]))
# by dynamic programming
def count_change_dp(n,arr):
    dp_dict = {}
    arr.sort()
    for num in arr:
        dp_dict[(num,0)] = 1
    for i in range(len(arr)):
        for j in range(n+1):
            if i == 0:
                if j % arr[i] == 0:
                    dp_dict[(arr[i],j)] = 1
                else:
                    dp_dict[(arr[i],j)] = 0
            else:
                if arr[i] > j :
                    dp_dict[(arr[i],j)] = dp_dict[arr[i-1],j]
                else:
                    dp_dict[(arr[i],j)] = dp_dict[arr[i-1],j] + dp_dict[arr[i],j-arr[i]]
    return dp_dict[(arr[-1],n)]
print(count_change_dp(100, [1, 5,10,25,50]))

def count_change_dp_other(n,arr):
    dp_dict = {}
    arr.sort()
    arr.insert(0,0)
    for num in arr:
        dp_dict[(num,0)] = 1
    for i in range(1,n+1):
        dp_dict[(0,i)] = 0
    for i in range(1,len(arr)):
        for j in range(n+1):
            if arr[i] > j :
                dp_dict[(arr[i],j)] = dp_dict[arr[i-1],j]
            else:
                dp_dict[(arr[i],j)] = dp_dict[arr[i-1],j] + dp_dict[arr[i],j-arr[i]]
    return dp_dict[(arr[-1],n)]
print(count_change_dp_other(100, [1, 5,10,25,50]))


# Write a function permute to compute all possible 
# permutations of elements of a given list.

def permutations(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        m = arr[i]
        remLst = arr[:i] + arr[i+1:]
        for p in permutations(remLst):
            result.append([m]+p)
    return result

#print(permutations(['a','b','c']))

def permute(a, l=0, r=0): 
    if r==0:
        r = len(a)-1
    if l==r: 
        print(a)
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]
#permute(['a','b'])