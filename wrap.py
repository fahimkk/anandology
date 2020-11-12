# Write a program wrap.py that takes filename and width
# as aruguments and wraps the lines longer than width

def wrap(filename, width):
    f=open(filename,'r')
    f_lines = f.readlines()
    for line in f_lines:
        line = line.strip('\n')
        start = 0
        for end in range(width,len(line),width):
            print(line[start:end])
            start = end
        if start != len(line):
            print(line[start:])
#wrap('she.txt',30)
#print('----')
# Can you write a new program wordwrap.py that works like wrap.py,
# but breaks the line only at the word boundaries?
def wordwrap(filename, width):
    f=open(filename,'r')
    f_lines = f.readlines()
    for line in f_lines:
        start = 0
        for word in line.split():
            start += len(word)+1 # +1 for space btw words
            if start <= width:
                print(word, end=' ')
            else:
                print()
                print(word,end=' ')
                start = len(word)
        print()
#wordwrap('she.txt',30)

# Write a program center_align.py to center align all lines in the given file.
#string.center(length, char), char- optional argument, bydefault= space
def center_align(filename):
    f=open(filename,'r')
    f_lines = f.readlines()
    width = 0 
    for line in f_lines:
        if len(line) > width: width = len(line)
    for line in f_lines:
        print(line.strip('\n').center(width))
center_align('she.txt')
