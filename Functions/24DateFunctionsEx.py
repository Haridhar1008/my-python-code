from datetime import date

d1 = date(1947,8,15)
d2 = date.today()
print("Given Date :", d1)
print("Today Date :", d2)

#attributes
print("\nDay :", d2.day)
print("Month :", d2.month)
print("Year :", d2.year)

#dateObj.strftime()
print("formated date :", d1.strftime('%d-%b-%Y'))
print("formated date :", d2.strftime('%d/%m/%Y'))

print("\nweek day  :", d1.strftime('%A'))
print("month name :", d1.strftime('%B'))
