import sys
try:
    a = {1:'Red', 2:'Green', 3:'Blue'}
    i = int(input("Enter a key :"))
    print(a[i])

except KeyError:
    print("invalid key.")

except Exception as x:
    print(x)
    print(sys.exc_info())    
    
