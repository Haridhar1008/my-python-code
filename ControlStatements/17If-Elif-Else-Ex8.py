#Accept three numbers from user and display the second largest number.

n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))
n3 = int(input("Enter 3rd number : "))

if n1 > n2 and n1 < n3 or n1 < n2 and n1 > n3:
    print(f'{n1} is second largest number')
elif n2 > n1 and n2 < n3 or n2 < n1 and n2 > n3:
    print(f'{n2} is second largest number')
else:
    print(f'{n3} is second largest number')
    
