#function definition

#write a function to accept radius of circle and return area.
def cir_area(radius):
    area = 3.14 * (radius ** 2)
    return area

#write a function to accept height and base of triange and return area.
def tri_area(base, height):
    area = 0.5 * base * height
    return area

#function calling 1
x = cir_area(7.81)
print("Area of circle is", x)

y = tri_area(6.5, 12)
print("\nArea of triangle is", y)

#function calling 2
r = float(input("\nEnter radius of circle : "))
p = cir_area(r)
print("Area of circle is", p)

b = float(input("\nEnter base of triangle : "))
h = float(input("Enter height of triangle : "))
q = tri_area(b, h)
print("Area of triangle is", q)
