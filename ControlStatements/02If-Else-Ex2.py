'''Accept values of length and breadth from user and check if it is
square or rectangle.'''

a = float(input("Enter length : "))
b = float(input("Enter breadth : "))

# ==
if a == b:
    print('It is square')
else:
    print('It is rectangle')

# !=
if a != b:
    print('It is rectangle')
else:
    print('It is square')
