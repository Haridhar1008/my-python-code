import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatyear(2025))


print(cal.formatyear(2025, 3, 2, 15, 4))


#print(cal.formatyear(2024, w=3, l=2, c=15, m=4))


print(cal.formatyear(2025, l=2))


#to display one year cal
print(calendar.calendar(2025))

