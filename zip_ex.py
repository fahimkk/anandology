# Write a python program zip.py to create a zip file. 
# The program should take name of zip file as first 
# argument and files to add as rest of the arguments.

def zip_file(arr):
    import zipfile
    f = zipfile.ZipFile('zipfile.zip','a')
    for file in arr:
        f.write(file,compress_type=zipfile.ZIP_DEFLATED)
#zip_file(['she.txt','reverse_she.txt'])

import zipfile
f = zipfile.ZipFile('zipfile.zip')
for name in f.namelist():
    print(name)
