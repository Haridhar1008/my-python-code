#Write a program to check whether a given character is alphabet or not.

ch = input("Enter a character : ")[0]
print(ch)
print(ord(ch))

#ex1
if ord(ch) >= 65 and ord(ch) <= 90 or ord(ch) >= 97 and ord(ch)<=122:
    print(f"{ch} is an alphabet")
else:
    print(f"{ch} is not an alphabet")

#ex2
if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z':
    print(f"{ch} is an alphabet")
else:
    print(f"{ch} is not an alphabet")
