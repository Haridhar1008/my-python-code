from datetime import *

dt1 = datetime(1947,8,15,1,20,30)
dt2 = datetime.now()
print("Given Datetime : {}\nNow Datetime : {}".format(dt1, dt2))

#after 77 days 
x = dt2 + timedelta(days=77)
print("\nAfter 77 days :", x)

#before 3 weeks 6 days
y = dt2 - timedelta(weeks = 3, days=6)
print("\nBefore 3weeks and 6Days :", y)

#after 2hours and 30minutes
z = dt2 + timedelta(hours = 2, minutes = 30)
print("\nAfter 2hours and 30 minutes :", z)

#date difference
d = dt2 - dt1
print("\nDate difference :", d)
print("Type of d :", type(d))

print("\nDate difference days :", d.days)
print("\nDate difference days in years :", d.days/365)
