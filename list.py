'''my_list=["apple","mango","cherry"]
print(my_list)

hello=[12,56,78,3456,6879977,23]
print(hello)

hi=[67.9,78.9,23.90]
print(hi)

boobalan=[56,89,9.0,67,89.0,"hello im sasi",True,False,"!@#$%^&*(#$%^&*("]
print(boobalan)'''

from pickle import FALSE


'''sasi=["hi","hello","how are u",78786,90.0,True,FALSE]
print(type(sasi))'''


'''print(fruits[1])
print(fruits[0:3])
print(fruits[-1])
print(fruits[-1:-4])
print(fruits[2:])
print(fruits[:-2])'''


#insert
fruits=["onion","banana","mango","strawberry","kiwi","cherry"]
fruits[1:3]="sasi","boobalan"
print(fruits)

fruits.insert(2,"mani")
print(fruits)

#append
fruits.append("hello im sasi")
print(fruits)

#extend
fruits=["cherry","mango"]
fruits2=["apple","kiwi"]
fruits.extend(fruits2)
print(fruits)

#index based removed
fruits.pop(1)
print(fruits)

#remove
fruits.remove("kiwi")
print(fruits)

#clear
fruits.clear()
print(fruits)

