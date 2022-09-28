'''#class bundle of objects and functions works over those object
class kart:
    __account=""
    __address=""
    __items=[]
    def setAccount(self,name):
        self.__account=name
    def setAddress(self,loc):
        self.__address=loc
    def setItems(self,it):
        self.__items=it
    def getAccount(self):
        return self.__account
    def getAddress(self):
        return self.__address
    def getItems(self):
        return self.__items
    def details(self):
        print(self.__account,self.__address,self.__items)

k1=kart()
k1.setAccount("boobalan")
k1.setAddress("tiruchengode")
k1.setItems(["hp","lenovo","asus"])

#k1.__account="sasikumar"
#k1.__address="tiruchengode"
#k1.__items.append("bata");k1.__items.append("Hp pendrive");k1.__items.append("rebok")
#print(k1.__account,k1.__address,k1.__items)
k1.details()

k2=kart()
k2.setAccount("sasikumar")
k2.setAddress("salem")
k2.setItems(["vall","vaio","dell","wallpaper"])
print(k2.getAccount(),k2.getItems(),k2.getAddress())'''

#return
def my_function(x):
    return 6*x
print(my_function(3))
print(my_function(5))
print(my_function(9))