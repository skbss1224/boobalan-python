''' 1
    22
    333
    4444
    55555'''
    
'''rows=6
for i in range(rows):
    for j in range(i):
        print(i,end=" ")
    print("")'''
    
'''
1
12
123
1234
12345
'''
'''rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print('')'''
    
'''for step in range(1,6):
    num=1
    for stone in range(1,6):
        print(num,end="")
        num=num+1
    print()'''
    
n=int(input("enter the number of row:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1