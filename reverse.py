# Write a program reverse.py to print lines of a file in reverse order
import sys

def reverse_txt(filename):
    f = open(filename,'r')
    f_list = f.readlines()
    for line_num in range(len(f_list)-1,-1,-1):
        print(f_list[line_num].strip('\n'))
    f.close()

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print('Usage: python filename.py filemane.txt')
    elif len(args) > 2:
        print('Usage: python filename.py filemane.txt')
    else: 
        filename = args[1]
        reverse_txt(filename)