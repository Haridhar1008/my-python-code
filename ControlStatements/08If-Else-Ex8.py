'''Accept a integer from user and check whether the given number is
in between 1 and 7 or not.'''

n = int(input("Enter a integer : "))

#and
if n >= 1 and n <= 7:
    print(f'{n} is in between 1 and 7')
else:
    print(f'{n} is not in between 1 and 7')

#or
if n < 1 or n > 7:
    print(f'{n} is not in between 1 and 7')
else:
    print(f'{n} is in between 1 and 7')
