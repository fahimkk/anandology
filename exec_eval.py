#exec
exec('x=1')
print(x)
print(x+7)

dict_1 = {'a':42}
print(dict_1)
exec('x=a+1',dict_1)
print(dict_1['x'])

code = 'def add_%d(x): return x + %d'
for i in range(1,5):
    exec(code %(i,i))
print(add_2(3))

#eval
print(eval('2+3'))
a = 2
print(eval('a*a'))
dict_2 = {'x':42}
s = eval('x+1',dict_2)
print(s)