from array import *

class source:
    def __init__(self) -> None:
        self.transactions=array('f',[])
    def __str__(self) -> str:
        strs=""
        for hai in self.transactions:strs+=str(hai)+"\n"
        return strs
class credit(source):
    def __init__(self) -> None:
        super(credit,self).__init__()
    def __add__(self,other):
        self.transactions.append(other)
    def __mul__(self,other):
        if len(self.transactions)>=8:
            extra=self.tansactions[len(self.transactions)-1]*other/100
            new=self.transactions[len(self.transactions)-1]+extra
            self.transactions.append(new)
            print(extra,"added to your account for the intrest of",other)
        else:
            print("intrest can't apply")
class debit(source):
    def __init__(self) -> None:
        super(debit,self).__init__()
    def __sub__(self,other):
        self.transactions.append(other)
    def __mul__(self,other):
        if len(self.transactions)>=5:
            reduce=self.transactions[len(self.transactions)-1]*other/100
            new=self.transactions[len(self.transactions)-1]-reduce
            self.transactions.append(new)
            print(reduce,"debited from your account intrest of ",other)
        else:print("intrest can't apply")
class user(debit,credit):
    def check(self):
        print("user function is called")
        
u=user()
u.check()
u+100
u-90
u+2000
u+3000
u*5.8
print(u)

'''        
c=credit()
c+12000
c+4500
print(c)'''

deb=debit()
deb-100
deb-100
deb-100
deb-100
deb-100
deb-100
deb-100
print(deb)