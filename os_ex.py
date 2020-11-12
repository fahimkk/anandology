import os
#print(os.getcwd.__doc__)
#print(dir(os))
#print(os.popen('ls').read())

# Write a program to list all files in the given directory
def list_files(directory):
    import os
    return os.listdir(directory)
#print(list_files('/home/fahim/Downloads'))

# Write a program extcount.py to count number of files for each 
# extension in the given directory. The program should take a 
# directory name as argument and print count and extension for
# each available file extension.
def extcount(path):
    import os
    dir_list = os.listdir(path)
    extcount_dict = {}
    for file in dir_list:
        ext = os.path.splitext(file)[1].strip('.')
        if ext:
            extcount_dict[ext] = extcount_dict.get(ext,0)+1
        else: 
            extcount_dict['folders'] = extcount_dict.get('folders',0)+1
    return extcount_dict
#print(extcount('/home/fahim/Downloads'))

# Write a program to list all the files in the given directory 
# along with their length and last modification time. 
# The output should contain one line for each file containing 
# filename, length and modification date separated by tabs.
def file_details(path):
    import os
    from datetime import datetime
    dir_list = os.listdir(path)
    for file in dir_list:
        filename = file
        file_path = os.path.join(path,file)
        details = os.stat(file_path)
        length = details.st_size
        modification = datetime.fromtimestamp(details.st_mtime)
        print(f'{filename}\t{length}\t{modification}')
#file_details('/home/fahim/lectureNotes')

# Write a program to print directory tree. 
# The program should take path of a directory as argument 
# and print all the files in it recursively as a tree.

def print_directory_tree(path):
    j=1
    for foldernames, subfoldernames, filenames in os.walk(path):
        print(f'{os.path.split(foldernames)[1]}')

        i = 1
        for filename in filenames:
            print(f'{" "*i}|--{filename}')
        for foldername in subfoldernames:
            print(f'{" "*i}|--{foldername}')
            i+=2
print_directory_tree('/home/fahim/tutorial/automateTheBoringStuff/pdffiles')