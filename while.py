'''print(1)
print(2)
print(3)
print(4)
print(5)'''

#while loop
'''a=1
while(a<=100):
    print(a)
    a=a+1'''
    
'''a=1
while(a<=1000):
    print(a)
    a=a+1'''
    
'''a=0
while(a<=100):
    print("even numbers",a)
    a=a+2'''

'''a=1
while(a<=100):
    print("add numbers:",a)
    a=a+2'''
    
#bus reservation
'''seats=1
while seats<=10:
    fare=int(input("enter the amount:"))
    if fare>=250 and fare<600:
        print("you can travel seater class in the bus",seats)
        seats+=1
    elif fare>=600:
        print("you can travel sleeper class in the bus",seats)
        seats+=1
    else:
        print("insuffiecient amount in this bus")
else:
    print("bus has started its journey")'''
    
#continue and break
from ast import Break


seat=1
while seat<=100:
    if seat%10==0:
        print("booked by online already",seat)
        seat+=1
        #break
        continue
    else:
        print("can be booked as open ticket",seat)
        seat+=1