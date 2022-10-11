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

p=penquin()
p.run()
p.sasi()
p.swim()
p.whoisthis()