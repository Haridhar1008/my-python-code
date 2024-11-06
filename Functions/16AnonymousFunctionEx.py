#function definition
cir_area = lambda radius: 3.14 * (radius**2)
tri_area = lambda base, height: 0.5 * base * height

#function calling 1
x = cir_area(6.88)
print("Area of circle is ", x)

y = tri_area(5.6, 9)
print("Area of triangle is ", y)
