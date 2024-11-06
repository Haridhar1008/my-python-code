#Positional/Required Arguments
def employee(eno, ename, esal):
    hra = esal*8/100
    da = esal*10/100
    pf = esal*11/100
    print("\n--- Employee Info ---\nEmp Id : {}\nEmp Name : {}\nEmp Sal : {}\nHRA : {:.2f}\n\
DA : {:.2f}\nPF : {:.2f}".format(eno, ename,esal, hra, da, pf))


#function calling 1
employee(1001, 'Pooja', 57000.55)

#function calling 2 (missing required argument)
#employee(1002, 'Veni')

#function calling 3 (missing positional argument)
#employee(1003,  58000.55, 'Mounika')
#employee('Mounika',58000.55, 1003)
