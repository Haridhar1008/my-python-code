'''Write a program to accept a character from user and check whether
it is upper case alphabet, lower case alphabet, digit or
special character'''

ch = input("enter a character : ")[0]
print(ch)

if ch >= 'A' and ch <= 'Z':
    print(f'{ch} is an upper case alphabet')
elif ch >= 'a' and ch <= 'z':
    print(f'{ch} is a lower case alphabet')
elif ch >= '0' and ch <= '9':
    print(f'{ch} is digit')
else:
    print(f'{ch} is special character/symbol')
