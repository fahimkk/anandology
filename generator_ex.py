def foo():
    print('begin')
    for i in range(3):
        print('before yeild', i)
        yield i
        print('after yeild', i)
    print('end')
f = foo()
#print(next(f))
#print('----')
#print(next(f))

def integers():
    """Infinite sequence of integers"""
    i = 1
    while True:
        yield i
        i +=1
def squares():
    for i in integers():
        yield i*i

def take(n,seq):
    """Returns first n values from the given sequence"""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

#print(take(5, squares()))

pythogorian_triplets = ((x,y,z) for z in integers() for y in range(1,z) for x in range(1,y) if x*x+y*y==z*z)
#print(take(5,pythogorian_triplets))

# cat and grep functions without generator
def cat(filenames):
    for f in filenames:
        for line in open(f):
            print(line,end='')
#cat(['she.txt','reverse_she.txt'])
def grep(pattern, filenames):
    for f in filenames:
        for line in open(f):
            if pattern in line:
                print(line, end='')
#grep('She',['she.txt','reverse_she.txt'])

# with generator
def read_files(filenames):
    for f in filenames:
        for line in open(f):
            yield line
def grep_generator(pattern,lines):
    return (line for line in lines if pattern in line)
def cat_generator(lines):
    for line in lines:
        #print(line,end='')
        print(line)

def main(pattern, filenames):
    lines = read_files(filenames)
    lines = grep_generator(pattern,lines) # commenout this will give all the line
    cat_generator(lines)

#main('She',['she.txt','reverse_she.txt'])

# Write a program that takes one or more filenames as arguments 
# and prints all the lines which are longer than 40 characters
def find_longer_line(lines,width):
    return (line for line in lines if len(line)>width)

def print_longer_line(filename, width):
    lines = read_files(filename)
    lines = find_longer_line(lines, width)
    cat_generator(lines)

#print_longer_line(['she.txt','reverse_she.txt'],45)

# Write a function findfiles that recursively descends the 
# directory tree for the specified directory and generates 
# paths of all the files in the tree.
import os
def findfiles(directory):
    for folders, subfolders, filenames in os.walk(directory): 
        for filename in filenames:
            yield filename
def findfiles_list_comprehension(directory):
    return (filename for folders,subfolders,filenames in\
        os.walk(directory) for filename in filenames)

def print_files(directory):
    filenames = findfiles(directory)
    #filenames = findfiles_list_comprehension(directory)
    cat_generator(filenames)

#print_files('/home/fahim/tutorial/anandology')

# Write a function to compute the number of python files 
# (.py extension) in a specified directory recursively.
def check_ext(filenames,ext):
    import os
    return (filename for filename in filenames if os.path.splitext(filename)[-1]==ext)
def count(arr):
    count_num = 0
    for _ in arr:
        count_num+=1
    return count_num

def count_file(directory,ext):
    filenames = findfiles_list_comprehension(directory)
    filenames = check_ext(filenames,ext) 
    print(count(filenames))
count_file('/home/fahim/tutorial/anandology','.py')

# Write a function to compute the total number of lines of code
# in all python files in the specified directory recursively
def count_line(directory,ext):
    filenames = findfiles_list_comprehension(directory)
    filenames = check_ext(filenames,ext)
    lines = read_files(filenames)
    print(count(lines))

count_line('/home/fahim/tutorial/anandology','.py')

# Write a function to compute the total number of lines 
# of code, ignoring empty and comment lines, in all python 
# files in the specified directory recursively.
def check_comment_empty_line(lines):
    return (line for line in lines if not line.startswith('#') and not line=='')
def count_line_without_comment_empty(directory,ext):
    filenames = findfiles_list_comprehension(directory) 
    filenames = check_ext(filenames,ext)
    lines = read_files(filenames)
    lines = check_comment_empty_line(lines)
    print(count(lines))

count_line_without_comment_empty('/home/fahim/tutorial/anandology','.py')

# Write a program split.py, that takes an integer n and 
# a filename as command line arguments and splits the 
# file into multiple small files with each having n lines.
def write(lines,n):
    i=1
    file_num = 1
    f = open(f'split_file_{file_num}','w')
    for line in lines:
        if i <= n:
            f.write(line)
            i+=1
        else:
            file_num +=1
            f = open(f'split_file_{file_num}','w')
            f.write(line)
            i = 2 # we written 1st line

def split(filename, n):
    filename = [filename]
    lines = read_files(filename)
    write(lines,n)

split('split_test.txt',4)

