from datetime import datetime

#datetime.strptime()
dob = datetime.strptime(input("Enter date of birth(dd/mm/yyyy \
hh:mm:ss) : "), '%d/%m/%Y %H:%M:%S')
print("dob = {}\ntype of dob = {}".format(dob, type(dob)))

doj = datetime.strptime(input("\nEnter date of join(dd-mm-yyyy) : "),\
                        '%d-%m-%Y')
print("\ndoj = {}\ntype of doj = {}".format(doj, type(doj)))
