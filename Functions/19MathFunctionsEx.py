#abs()
print("abs of 120 - 35 : ", abs(120-35))
print("abs of 35 - 120 : ", abs(35 - 120))

import math
#fabs()
print("\nabs of 120 - 35 : ", math.fabs(120-35))
print("abs of 35 - 120 : ", math.fabs(35 - 120))

#round()
print("\nround of 3.4 : ", round(3.4))
print("round of 3.8 : ", round(3.8))
print("round of 3.5 : ", round(3.5))

print("\nround of 3.443983 : ", round(3.443983, 2))
print("round of 3.447983 : ", round(3.447983, 3))

#ceil()
print("\nceil of 3.4 : ", math.ceil(3.4))
print("ceil of 3.8 : ", math.ceil(3.8))

#floor()
print("\nfloor of 3.4 : ", math.floor(3.4))
print("floor of 3.8 : ", math.floor(3.8))

#pow()
print("\npow of 3,4 : ", math.pow(3,4))

#sqrt()
print("\nsqrt of 25 : ", math.sqrt(25))
print("sqrt of 30 : ", math.sqrt(30))

#exp()
print("\nexp of 2 :", math.exp(2))

#log()
#log10()
print("\nlog(2) :", math.log(2))
print("log10(2) :", math.log10(2))

#max()
#min()
print("\nmax :", max(92,66,56,91,67,89,66,92,66))
print("min :", min(92,66,56,91,67,89,66,92,66))

#pi
print("\npi :", math.pi)
print(22/7)

#Find area of circle
r = float(input("\nEnter radius of circle : "))
area = math.pi * math.pow(r,2)
print("Area of circle is ", area)

