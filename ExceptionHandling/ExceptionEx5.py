try:
    val = int(input("Enter a value(b/w 1 and 7) : "))

    if val<1 or val>7:
       raise Exception("value should be in between 1 and 7")
    else:
        print("Value = ",val)
except Exception as ex:
   print("Error :", ex)
