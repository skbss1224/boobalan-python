print("--------wecome to loan agency---------")
salary=int(input("tell us monthly salary:"))
file=bool(input("are you paying your tax properly:"))
print("are you elligible for personal loan of 1L",((salary>=15000)or(file==True)))
print("are you elligiblr for business loan of 10L",((salary>=50000)and(file==True)))
print("are you elligible for home loan of 5L",((salary>=20000 and salary<=40000)))