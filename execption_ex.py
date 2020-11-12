try:
    print ("a")
except:
    print ("b")
else:
    print ("c")
finally:
    print ("d")

print('--------')

try:
    print("a")
    raise Exception("doom")
except:
    print("b")
else:
    print("c")
finally:
    print("d")

print('--------')

def f():
    try:
        print("a")
        return
    except:
        print("b")
    else:
        print("c")
    finally:
        print("d")

f()