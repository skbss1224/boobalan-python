#class and objects
#instance variable

'''class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        print(max_speed,mileage)
modelx=vehicle(240,18)
print("maximum speed:",modelx.max_speed,"mileage:",modelx.mileage)'''

'''
#pass key word
class vehicle:
    pass

def hello():
    pass


#inheritance in python
class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class bus(vehicle):
     print("hello im sasi")
school_bus=bus(" volvo",180,12)
print("vehicle name",school_bus.name,"speed",school_bus.max_speed,"mileage",school_bus.mileage)'''

#default parameter



class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        print(name)
    def seating_capacity(self,capacity):
        print(capacity)
        print(self.name)
        print(self.max_speed)
        print(self.mileage)
        
hello=vehicle("sasi",67,78)
hello.seating_capacity(20)