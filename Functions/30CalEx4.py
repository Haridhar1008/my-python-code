import calendar

print("**** Months ****")
for m in calendar.month_name:
        print(m)

x = [m for m in calendar.month_name if m != '']
print(x)


print("\n**** Week Days ****")
for wd in calendar.day_name:
        print(wd)

y = [wd for wd in calendar.day_name]
print(y)

