class BankAccount:
    def __init__(self):
        self.balance = 0
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    def deposite(self,amount):
        self.balance += amount
        return self.balance

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance
    def withdraw(self,amount):
        if self.balance - amount < self.minimum_balance:
            print('sorry minimum balance must be maintained')
        else:
            BankAccount.withdraw(self,amount)

a = MinimumBalanceAccount(1000)
#print(a.balance)
#a.withdraw(500)
a.deposite(2000)
#print(a.balance)
a.withdraw(500)
#print(a.balance)

class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'
a = A()
b = B()
#print(a.f(), b.f())
#print(a.g(), b.g())

# Drawing Shapes
class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[' ']*width for i in range(height)]
    def setpixel(self, row, col):
        self.data[row][col] = '*'
    def getpixel(self,row, col):
        return self.data[row][col]
    def display(self):
        print('\n'.join([''.join(row) for row in self.data]))
x = Canvas(5,3)
x.setpixel(0,0)
x.setpixel(1,1)
x.setpixel(2,2)
x.setpixel(2,2)
#print(x.data)
#x.display()

class RationalNumber:
    """ Rational Numbers with support for arthmetic 
        operations.
        a = RationalNumber(1,2)
        b = RationalNumber(1,3)
        a+b = 5/6
        a-b = 1/6
        a*b = 1/6
        a/b = 3/2"""
    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator
    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)
        n = self.n*other.d + self.d*other.n 
        d = self.d*other.d
        return RationalNumber(n,d)
    def __sub__(self, other):
        if not isinstance(other,RationalNumber):
            other=RationalNumber(other)
        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2 - n2*d1, d1*d2)
    def __mul__(self, other):
        if not isinstance(other,RationalNumber):
            other=RationalNumber(other)
        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*n2, d1*d2)
    def __div__(self, other):
        if not isinstance(other,RationalNumber):
            other=RationalNumber(other)
        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2, d1*n2)
    def __str__(self):
        return "%s/%s" %(self.n, self.d)
    __repr__ = __str__

a = RationalNumber(1,2)
b = RationalNumber(1,3)
print(a*b)
print(a)
print(a+5)
