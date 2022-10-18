'''try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")'''
    
from logging import exception

'''
x=-1
if x<0:
    raise exception ("sorry ,no numbers below zero")'''
    
'''x="hahsa"
if not type(x) is int:
    raise TypeError ("only integers are allowed")'''

'''
try:
    div=4//0
    print(div)
except ZeroDivisionError:
    print("atepting to devide by zero")
finally:
    print("this code of finally caluse")
    
def hello(num1):
    try:
        hi=1/num1
    except ZeroDivisionError:
        print("we cannot devided by zero")
    else:
        print(hi)
hello(4)
hello(0)'''

try:
    print("try block")
    x=int(input("enter a number:"))
    y=int(input("enter the another value:"))
    z=x/y
except ZeroDivisionError:
    print("division by 0 not accepted")
finally:
    print("finally block")
    x=0
    y=0
    print("out of try,except,else and finally blocks")
    
    