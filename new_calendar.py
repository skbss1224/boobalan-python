'''from datetime import time
a=time()
print("seconds",a)

#time (hour ,minute and seconds)
b=time(11,34,56)
print("b=",b)

#time (hour ,minute and seconds)
c=time(hour=11,minute=34,second=56)
print("c=",c)

#time (hour ,minute ,seconds,microsecond)
d=time(11,34,56,12345)
print("d=",d)'''

from datetime import datetime
import pytz

local=datetime.now()
print("local:",local.strftime("%d/%m/%y,%H:%M:%S"))

tz_NY=pytz.timezone("America/New_york")
datetime_ny=datetime.now(tz_NY)
print("NY:",datetime_ny.strftime("%d/%m/%y,%H:%M:%S"))

tz_London=pytz.timezone("Europe/London")
datetime_London=datetime.now(tz_London)
print("London:",datetime_London.strftime("%d/%m/%y,%H:%M:%S"))