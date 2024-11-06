from datetime import datetime

dt1 = datetime(1947,8,15,1,20,30)
dt2 = datetime.now()
print("Given Datetime :", dt1)
print("Now Datetime :", dt2)

#dtObj.strftime()
print("\nFormated datetime :", dt1.strftime('%d/%m/%y %I:%M:%S %p'))
print("\nFormated datetime :", dt2.strftime('%d-%b-%Y %I:%M:%S %p'))

print("\nweek day of dt1 :", dt1.strftime('%A'))
print("week day of dt1 :", dt1.strftime('%a'))

print("\nweek day of dt2 :", dt2.strftime('%A'))
print("week day of dt2 :", dt2.strftime('%a'))

print("\nMonth name of dt1 :", dt1.strftime('%B'))
print("Month name of dt2 :", dt2.strftime('%b'))

print("\nMonth and year :", dt1.strftime('%B - %Y'))
print("Month and year :", dt2.strftime('%B - %Y'))

print("\nLocal Date and time :", dt2.strftime('%c'))
print("Local Date :", dt2.strftime('%x'))
print("Local time :", dt2.strftime('%X'))
