import datetime

dt1 = datetime.datetime(1947,8,15,1,20,40)
print("Given Datetime :", dt1)

#attributes
print('\nDay :', dt1.day)
print('Month :', dt1.month)
print('Year :', dt1.year)

print('\nHour :', dt1.hour)
print('Minute :', dt1.minute)
print('Second :', dt1.second)
print('Microsecond :', dt1.microsecond)

#Built-in Functions and Methods

#datetime.now()
dt2 = datetime.datetime.now()
print("\nNow datetime :", dt2)

#datetime.today()
dt3 = datetime.datetime.today()
print("Today Datetime :", dt3)

#datetime.utcnow()
dt4 = datetime.datetime.utcnow()
print("Utcnow Datetime :", dt4)

#dtObj.weekday() [mon --> 0, tue --> 1, wed --> 2, ..... sun --> 6]
x = dt1.weekday()
y = dt2.weekday()
print("\nweeday of dt1 : {}\nweekday of dt2 : {}".format(x, y))

week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print("\nweeday of dt1 : {}\nweekday of dt2 : {}".format(week[x],\
                                                         week[y]))
#dtObj.date()
d = dt2.date()
print("\nOnly date :", d)

#dtObj.time()
t = dt2.time()
print("Only time :", t)

#datetime.combine()
dt = datetime.datetime.combine(d,t)
print("after combine d and t :", dt)
