'''print("*******GANGA THEATER*******")
def sasi():
    print("iam sasi")
    age=int(input("enter your age:"))
    if(age>=18):
        print("your age is above eighteen")
        movie=input("enter the movie name:")
        if("aasique"==movie):
            print("you are allowed this movie watching")
        else:
            print("you are selected another movie name")
    else:
        print("you are is under eighteen")

def boobalan(name,secondname):
    print("iam boobalan")
    print(name,"this is parameter passing")
    print(secondname,"this is second name")
    amount=int(input("enter your amount:"))
    if(50000<=amount):
        print("you have withdraw this amount")
    else:
        print("you are not aloowed to withdraw this amount")
 
boobalan(name="this is boobalan",secondname="bala")     
sasi()
sasi()'''

def marks(english,math=85,science=80):
    print("marks in:english is-",english,"math-",math,"science-",science)
marks(71)
marks(65,science="75")