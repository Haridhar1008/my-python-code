try:    
    import sys
    #import system  
    from datetime import datetime
    dt = datetime.now()
    print(dt.day)
    print(dt.year)
    print(dt.days) #attribute error

except ModuleNotFoundError:
    print("Module not found")
    
except AttributeError:
    print("no such attribute...")
    
except Exception as x:
    print(x)
    print(sys.exc_info())    
    
