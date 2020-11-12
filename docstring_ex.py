# Write a program mydoc.py to implement the functionality of pydoc. 
# The program should take the module name as argument and print 
# documentation for the module and each of the functions defined in that module.


import inspect

def documentation(doc_str):
    module = __import__(doc_str)
    print(f'Help on module {module.__name__}')
    print()
    print('DESCRIPTION')
    print()
    print(module.__doc__)
    print()
    print('FUNCTIONS')
    print()
    dir_list = dir(module)
    for instant in dir_list:
        # eval is used to convert string into its object
        # inspect.isfuction is only work for object
        instant=eval(f'module.{instant}')
        if inspect.isfunction(instant):
            print(f'{instant.__name__}()')
            print(instant.__doc__)
            print()


documentation('num')
