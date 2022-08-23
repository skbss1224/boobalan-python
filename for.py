#for loop
'''fruits=["apple","banana","cherry"]
for sasi in fruits:
    print(sasi)'''
    
'''for sasi in "banana":
    print(sasi,end=" ")'''
    
'''fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        #break
        continue'''
    
'''for x in range (0,100):
    print(x)'''
'''
for x in range (10,100):
    print(x)'''
    
    
'''for x in range(2,30,3):
    print(x)'''
'''   
for x in range(1,100,2):
    print("add numbers",x)'''
    
    
'''   
for x in range(0,100,5):
    print("even numbers",x)'''
    
    
start=int(input("tell us start range:"))
limit=int(input("tell us prime end point:"))
if limit>=start:
    for num in range(start,limit+1):
        if num==2 or num==3 or num==5 or num==7 or num %2!=0 and num %3!=0 and num %5!=0 and num %7!=0:
            print(num,end=" ")
else:
    print("invalid start and limit")
        