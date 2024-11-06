#function definition
def employee(eno, ename, esal):
    'This function displays given employee details'
    print('\n--- Employee Details ---\nEmp Id : {}\nEmp Name : {}\n\
Emp Salary : {}'.format(eno, ename, esal))
    
#function calling 1
employee(1001, 'Veni', 59000.55)

#function calling 2
x = int(input("\nEnter employee id : "))
y = input("Enter employee name : ")
z = float(input("Enter employee salary : "))
employee(x, y, z)
