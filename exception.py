
'''ramdomlist=['a',0,2]

for entry in ramdomlist:
    try:
        print("the entry is",entry)
        r=1/int(entry)
        break
    except Exception as a :
        print(entry)
        print("next entry")
        print()
print("entry",entry,"is",r)'''
'''
while True:
    try:
        x=int(input(" enter a number:"))
        break
    except ValueError:
        print("oops don't use alphabet values")'''
        
while True:
    try:
        x=int(input("enter a number:"))
        print(x/0)
    except ZeroDivisionError:
        print("don't divided zero number")
    except ValueError:
        print("don't type alphabet values")
        