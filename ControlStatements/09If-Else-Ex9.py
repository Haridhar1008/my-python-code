'''Accept a string from user and display reverse string
and also check whether the given string is palindrome or not'''

s = input("Enter a string : ")

r = s[::-1]
print("Reverse string is ", r)

if s == r:
    print(f'{s} is palindrome')
else:
    print(f'{s} is not palindrome')
