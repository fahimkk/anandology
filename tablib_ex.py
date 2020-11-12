# tablib is used to work with csv and excel data
import tablib

# create a dataset
data = tablib.Dataset()

# add rows 
data.append(['A',1])
data.append(['B',2])
data.append(['C',3])

# adding header, if we provide header then its compulosry
# to provide header when append_col
data.headers=['name','rank']

# to print pythonic way,
print(data.dict)     

# to append a column, element should equal to no of rows
data.append_col(['a','b','c'],header='smll')
print(data.dict)     

print()
# selecting rows and columns  
print(data[0])
print(data['name']) # same as print(data.get_col(0))
print(data.headers)

# to delete data
#del data['smll']
# to delete a range of data
#del data[0:12]

print()
print(data.export('csv'))
print(data.export('json'))
print(data.export('yaml'))
# for xls and df pip install tablib[pandas]

# to write data
# we can either open the file in 'w' or in 'wb'
with open('tablib_test.csv','w') as f:
    # we can save file to all above formats.
    f.write(data.export('csv'))

# when opening a file
with open('tablib_test.csv','r') as g:
    imported_data = tablib.Dataset().load(g)
print(f'Imported_data: {imported_data.dict}')

# to create a multiple sheet in excel
#sheet1 = tablib.Dataset()
#sheet2 = tablib.Dataset()
#book = tablib.Databook([sheet1,sheet2])

# Dynamic columns
def rand_grade(row):
    # argument row is provided by the data.append_col itself
    import random
    return random.randint(60,100)
data.append_col(rand_grade, header='mark')
print(data.export('csv'))
