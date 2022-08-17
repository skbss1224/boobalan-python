print("----------------boobalan bus service------------")
place=input("enter the place:")
if(place=="chennai"):
    print("you are selected",place)
    type=input("enter the bus type:")
    if(type=="ordinary"):
        print("you are selected",type)
        amount=int(input("enter the amount:"))
        if(amount>=150):
            bal=amount-150
            print("you are 1 ticket reserved",type,"bus")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="delux"):
        print("you are selected",type)
        amount=int(input("enter the amount:"))
        if(amount>=250):
            bal=amount-250
            print("you are 1 ticket reserved",type,"bus")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="superdelux"):
        print("you are selected",type)
        amount=int(input("enter the amount:"))
        if(amount>=350):
            bal=amount-350
            print("you are 1 ticket reserved",type,"bus")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="sleeper"):
        print("you are selected",type)
        amount=int(input("enter the amount:"))
        if(amount>=450):
            bal=amount-450
            print("you are 1 ticket reserved",type,"bus")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    else:
        print("A/c bus service not available")
elif(place=="coimbatore"):
    print("you are selected",place)
    type=input("enter the bus type:")
    if(type=="ordinary"):
        print("you are selected",type)
        amount=int(input("enter the amount:"))
        if(amount>=100):
            bal=amount-100
            print("you are 1 ticket reserved",type,"bus")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="delux"):
        print("you are selected",type)
        amount=int(input("enter the amount:"))
        if(amount>=200):
            bal=amount-200
            print("you are 1 ticket reserved",type,"bus")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="superdelux"):
        print("you are selected",type)
        amount=int(input("enter the amount:"))
        if(amount>=300):
            bal=amount-300
            print("you are 1 ticket reserved",type,"bus")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="sleeper"):
        print("you are selected",type)
        amount=int(input("enter the amount:"))
        if(amount>=400):
            bal=amount-400
            print("you are 1 ticket reserved",type,"bus")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    else:
        print("A/c bus service not available")
else:
    print("only two place sevice available chennai and coimbatore")