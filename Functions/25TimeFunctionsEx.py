from datetime import time, datetime

t1 = time(10,34, 55)
t2 = datetime.now().time()

print("Given time :", t1)
print("Now time :", t2)

#attributes
print("\nHour :", t2.hour)
print("Minute :", t2.minute)
print("Second :", t2.second)
print("Microsecond :", t2.microsecond)

#timeObj.strftime()
print("\nformated time of t1 :", t1.strftime('%I:%M:%S %p'))
print("formated time of t2 :", t2.strftime('%I:%M:%S %p'))
