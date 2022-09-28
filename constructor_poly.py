#class with constructor and inner creation

#constructor:
#priority to execute before any other function to be called
# it will be initiated while creating object it self
#to initialise to members

#__str__,__del__,operator over loading

class loan:
    __loanAmt=0.0
    __loanNumber=0
    __loanIntrest=0.0
    __loanNeedToPay=0.0
    __loanBorrower=""
    __loanDuration=0
    def __init__(self,name="",num=0,dur=0,it=0.0,amt=0):
        print("initiated") 
        self.__loanBorrower=name;self.__loanNumber=num;self.__loanDuration=dur
        self.__loanIntrest=it;self.__loanAmt=amt;
        calc=self.getLoanAmt()*(self.getLoanIntrest())/100
        calc*=self.getLoanDuration()
        calc+=self.getLoanAmt()
        self.__loanNeedToPay=calc
    def __del__(self):
        print("object releasing from memory")
    def __str__(self) :
        return str(self.__loanNumber)+" "+self.__loanBorrower+" "+str(self.__loanDuration)+" "+str(self.__loanIntrest)+" "+str(self.__loanAmt)+" "+str(self.__loanNeedToPay)+"\n"
    def __add__(self,data=0):
        calc=self.getLoanAmt()*(self.getLoanIntrest())/100
        calc*=self.getLoanDuration()
        calc+=self.getloanAmt()
        self.__loanNeedToPay=calc
    def __xor__(self,data=""):
        return str(self.__loanNumber)+" "+self.__loanBorrower+" "+str(self.__loanDuration)+" "+str(
            self.__loanIntrest)+" "+str(self.__loanAmt)+" "+str(self.__loanNeedToPay)+"\n"
        
    def setLoanAmt(self,amt):self.__loanAmt=amt
    def getLoanAmt(self):return self.__loanAmt
    def setLoanNumber(self,num):self.__loanNumber=num
    def getLoanNumber(self):return self.__loanNumber
    def setLoanIntrest(self,it):self.__loanIntrest=it
    def getLoanIntrest(self):return self.__loanIntrest
    def getLoanNeedToPay(self):return self.__loanNeedToPay
    def setLoanNeedToPay(self,pay):self.__loanNeedToPay=pay
    def setLoanBorrower(self,borr):self.__loanBorrower=borr
    def getLoanBorrower(self):return self.__loanBorrower
    def setLoanDuration(self,years):self.__loanDuration=years
    def getLoanDuration(self):return self.__loanDuration
    

l1=loan()
'''l1.setLoanAmt(50000);l1.setLoanBorrower("boobalan");l1.setLoanDuration(3)
l1.setLoanIntrest(4.1);l1.setLoanNumber(34567856);
l1+1'''
calc=l1.getLoanAmt()*(l1.getLoanIntrest())/100
calc*=l1.getLoanDuration()
calc+=l1.getLoanAmt()
l1.setLoanNeedToPay(calc)
print(l1)

'''l2=loan("boobalan",2345678,3,13.1,45678)
print(l2^"hai")'''

l3=loan(amt=167887,it=4.5,num=234567,dur=4,name="sasi")
print(l3)