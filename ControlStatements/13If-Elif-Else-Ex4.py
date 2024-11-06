'''Write a program to input month name and print number of days in
given month.'''

#31 --> ('jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec')
#30 --> ('apr', 'jun', 'sep', 'nov')
#28/29  --> 'feb'

month = input("Enter a month name : ")
print(month)
m = month[:3].lower()
print(m)

if m in ('jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec'):
    print(f'{month} has 31 days')
elif m in ('apr', 'jun', 'sep', 'nov'):
    print(f'{month} has 30 days')
elif m == 'feb':
    print(f'{month} has 28/29 days')
else:
    print(f'{month} is not a month name')
