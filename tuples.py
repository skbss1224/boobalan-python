'''thistuple=("apple","banana","cherry")
print(thistuple)

hello=("apple","banana","cherry","apple","cherry")
print(hello)
print(len(hello))'''

'''this=("apple","banana")
print(type(this))'''

'''tuple1=("apple","banana","cherry")
tuple2=(1,5,7,9,3)
tuple3=(True,False,False)
print(tuple1)
print(tuple2)
print(tuple3)'''

'''
tuple1=("abc",34,True,40,"male")
print(tuple1)'''

'''tuple1=("apple","banana","cherry")
print(tuple1[1])
print(tuple1[-1])'''

'''thistuple=("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-1:-4])

if "apple" in thistuple:
    print("yes ,'apple' is in the fruits tuple")
'''    
#update
'''x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)'''

#append
'''thistuple=("apple","banana","cherry")
y=list(thistuple)
y.append("orange")
thistuple=tuple(y)
print(thistuple)'''

#remove

'''thistuple=("apple","banana","cherry")
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(thistuple)'''

#del
'''thistuple=("apple","banana","cherry")
del thistuple
print(thistuple)'''

'''fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)'''

#join
tuple1=("apple","b","c")
tuple2=(1,2,3)
tuple3=tuple1+tuple2
print(tuple3)
