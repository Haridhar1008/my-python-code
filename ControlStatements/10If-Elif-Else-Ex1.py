#Write a program to find minimum mark in given three subject marks.
m1 = int(input("Enter 1st subject marks : "))
m2 = int(input("Enter 2nd subject marks : "))
m3 = int(input("Enter 3rd subject marks : "))

if m1 < m2 and m1 < m3:
    print(f'{m1} is minimum mark')
elif m2 < m3:
    print(f'{m2} is minimum mark')
else:
    print(f'{m3} is minimum mark')
