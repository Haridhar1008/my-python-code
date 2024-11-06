import sys
try:
    x = int(input("Enter 1st integer : "))
    y = int(input("Enter 2nd integer : "))
    z = x/y
    print(z)
except ZeroDivisionError:
    print("Denominator should not be zero")
except ValueError:
    print("Invalid input value")
except Exception as ex:
    print(ex)
    print(sys.exc_info())
   
   
    
    
