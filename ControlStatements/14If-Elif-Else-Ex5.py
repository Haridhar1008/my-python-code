#Write a program to check whether a year is leap year or not.

year = int(input("Enter a year : "))

if year%100 == 0 and year%400 == 0:
    print(f'{year} is leap year')
elif year%100 != 0 and year%4 == 0:
    print(f'{year} is leap year')
else:
    print(f'{year} is not a leap year')
    
