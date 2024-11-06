import sys

try:
    a = 10
    b = "20"
    print(a + b)

except TypeError:
    print("invalid datatype")
    
except Exception as x:
    print(x)
    print(sys.exc_info())  
    
