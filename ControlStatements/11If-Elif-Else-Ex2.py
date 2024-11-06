'''Take input of 3 people ages from user and determine oldest
and youngest among them.'''

p1 = int(input("Enter age of 1st person : "))
p2 = int(input("Enter age of 2nd person : "))
p3 = int(input("Enter age of 3rd person : "))

#To find oldest 
if p1 > p2 and p1 > p3:
    print(f'{p1} is oldest person')
elif p2 > p3:
    print(f'{p2} is oldest person')
else:
    print(f'{p3} is oldest person')

#To find youngest
if p1 < p2 and p1 < p3:
    print(f'{p1} is youngest person')
elif p2 < p3:
    print(f'{p2} is youngest person')
else:
    print(f'{p3} is youngest person')
