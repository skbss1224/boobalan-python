class Bird:
    def __init__(self) -> None:
        print("bird is ready")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("swim faster")
        
class penquin(Bird):
    def __init__(self) -> None:
        print("penquin is ready")
    
    def sasi(self):
        print("penquin")
    def run(self):
        print("run faster") 
        
class peacock(penquin):
    def __init__(self) -> None:
        print("peacock is ready")
        
    def flying(self):
        print("pecock is flying")
    def peacock_food(self):
        print("peacock food eated")       

p=peacock()
p.flying()
p.peacock_food()
p.run()
p.sasi()
p.whoisthis()