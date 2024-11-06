#function definition

#to covert fahrenheit to celsius: c = (f-32)*(5/9)
def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

#to covert celsius to fahrenheit: f = c*(9/5) + 32
def to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

#Function Calling 1
x = to_celsius(101)
print(x)

#Function Calling 2
y = to_fahrenheit(38)
print(y)
