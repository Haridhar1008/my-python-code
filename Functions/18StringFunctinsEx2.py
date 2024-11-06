a = 'Sai Manoj'
b = 'amer'
c = 'GAYATHRI'
d = 'Varshita@123'
e = 'deepthi345'
f = '456'
g = ' '
h = '\u00bd'
print(a,b,c,d,e,f,g,h,sep='\n')

#isalnum()
print("\nb is alnum :", b.isalnum())
print("d is alnum :", d.isalnum())
print("e is alnum :", e.isalnum())
print("f is alnum :", f.isalnum())

#isalpha()
print("\na is alpha :", a.isalpha())
print("b is alpha :", b.isalpha())
print("d is alpha :", d.isalpha())
print("e is alpha :", e.isalpha())

#isdigit()
print("\nf is digit :", f.isdigit())
print("e is digit :", e.isdigit())
print("h is digit :", h.isdigit())

#isnumeric()
print("\nf is numeric :", f.isnumeric())
print("e is numeric :", e.isnumeric())
print("h is numeric :", h.isnumeric())

#islower()
print("\nb is lower :", b.islower())
print("c is lower :", c.islower())

#isupper()
print("\nb is upper :", b.isupper())
print("c is upper :", c.isupper())

#istitle()
print("\na is title :", a.istitle())
print("b is title :", b.istitle())

#isspace()
print("\ng is space :", g.isspace())
print("f is space :", f.isspace())

#join()
colors = ('red','green','blue','white','black')
print("\nbefore join, colors :", colors)
x = '@'.join(colors)
print("After join, colors :", x)

#split()
fruits = 'apple*mango*banana*orange*grapes'
print("\nbefore split, fruits : ", fruits)
y = fruits.split('*')
print("after split, fruits :", y)
for i in y:
    print(i)

#accept 3 integers by using only one input()
#ex 1
n = []
for i in range(3):
    a = int(input("Enter a integer : "))
    n.append(a)
print(n)

#ex 2
a,b,c = input("\nEnter 3 integers : ").split()
print('a = {}\nb = {}\nc = {}'.format(a,b,c))

#ex 3 (split user name and domain name and display)
email = 'abc123xyz@gmail.com'
p = email.split('@')
print("\nuser name :", p[0])
print("domain name :", p[1])

#center()
#ljust()
#rjust()
t = 'Student Info'
print(t)
print(t.center(40))
print(t.center(40,'*'))

print(t.ljust(40,'-'))
print(t.rjust(40,'='))

#strip()
#lstrip()
#rstrip()
t1 = '    IT POINT     '
t2 = '***@Dsnr***'
print(t1 + t2)
print(t1.strip() + t2.strip('*'))

print(t1.lstrip() + t2.lstrip('*'))
print(t1.rstrip() + t2.rstrip('*'))

#encode()
#decode()
pwd = 'abc123@xyz'
en = pwd.encode('utf-16')
print(en)

de = en.decode('utf-16')
print(de)

