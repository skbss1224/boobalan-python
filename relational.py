#relational operators
from ast import operator


'''<-lessthan operator
>-greaterthan operator
<=-lessthan equal operator
>=-greaterthan equal operator
==-equal operator'''
'''tamil=int(input("enter the tamil mark:"))
english=int(input("enter the english mark:"))
maths=int(input("enter the maths mark:"))
science=int(input("enter the science mark:"))
social=int(input("enter the social mark:"))
print("lessthan operator:",tamil<english)
print("greater than operator",english>maths)
print("lessthan equal operator",maths<=science)
print("greaterthan equal operator",science>=social)
print("equal operator",social==tamil)'''

#control statement
'''mani=int(input("enter the mani mark:"))
vijay=int(input("enter the vijay mark:"))
manisha=int(input("enter the manisha mark:"))
gopal=int(input("enter the gopal mark:"))
if(mani<vijay):
    print("vijay is big mark to mani ")
elif(vijay>manisha):
    print("manisha less mark to vijay")
elif(gopal==manisha):
    print("manisha is big mark to gopal")
else:
    print("no one condition isn't true")'''
    
'''nationality=input("enter your nationality:")
if(nationality=="indian"):
    print("you are applied for voter id")
else:
    print("you are not a indian")
    print("better luck next time")'''
    
age=int(input("enter your age:"))
if(age>=18):
    print("you are elligible for +18")
    weight=int(input("enter your weight:"))
    if(weight>=50):
        print("you are donate your blood")
    else:
        print("you not elligible for your weight")
else:
    print("you not a 18+ , so you are not elligible for blood donating")   
