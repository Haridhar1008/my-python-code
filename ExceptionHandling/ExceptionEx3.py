import sys
try:    
    my_list = [10,30,50,70]
    
    i = int(input("Enter a index : "))
    print("Index {} has {}".format(i, my_list[i]))

except IndexError:
    print("Invalid index")
    
except Exception as ex:
    print(ex)
    print(sys.exc_info())    
    
