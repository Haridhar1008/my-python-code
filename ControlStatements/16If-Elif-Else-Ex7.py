'''Accept three sides of a triangle and check whether it is
an equilateral, isosceles or scalene triangle.

An equilateral triangle has all three sides are equal.
A scalene triangle has three unequal sides.
An isosceles triangle has two equal sides.'''

s1 = float(input("Ente side1 length of triangle : "))
s2 = float(input("Ente side2 length of triangle : "))
s3 = float(input("Ente side3 length of triangle : "))

if s1 == s2 == s3:
    print(f'It is an equilateral triangle')
elif s1 != s2 != s3 != s1:
    print(f'It is a scalene triangle')
elif s1==s2 and s1!=s3 or s1==s3 and s1!=s2 or s2==s3 and s2!=s1:
    print(f'It is an isosceles triangle')
