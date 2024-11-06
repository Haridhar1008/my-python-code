t ='student INFORMATION sysTEM'
stu_names = ['sHiVa pRiya', 'hAri pRIya', 'GAYATHRI', 'madhu b',
             'sindhu j', 'prashanth chintu', 'ranga Swamy']

#capitalize()
print("\nCapitalize :", t.capitalize())

print("\n-- Capitalized names--")
for s in stu_names:
    print(s.capitalize())

#title()
print("\nTitlecase :", t.title())

print("\n-- title --")
for s in stu_names:
    print(s.title())

#upper()
print("\nUppercase :", t.upper())

print("\n-- uppercase names --")
for s in stu_names:
    print(s.upper())
    
#lower()
print("\nLowercase :", t.lower())

print("\n-- lowercase names --")
for s in stu_names:
    print(s.lower())

print("\nString = ", t)
#swapcase()
print("\nSwapcase :", t.swapcase())

#len()
print("\nLength of t : ", len(t))
print("\n-- Length of names--")
for s in stu_names:
    print('{}({})'.format(s.capitalize(),len(s)))
    
#count()
print("\n-- No of a's in names --")
for s in stu_names:
    print("{} - no of a's ({})".format(s.capitalize(), \
                                        s.lower().count('a')))

#max()
for s in stu_names:
    print("Max : ", max(s))
    for ch in s:
        print('{} - {}'.format(ch, ord(ch)))
    else:        
        print('\n')
    
#min()
for s in stu_names:
    print("Min : ", min(s))
    for ch in s:
        print('{} - {}'.format(ch, ord(ch)))
    else:        
        print('\n')

email = 'abc123xyz@gmail.com'
print("\nemail :", email)

#startswith()
print("\nemail starts with abc1 :", email.startswith('abc1'))
print("email starts with 123 :", email.startswith('123'))

#endswith()
print("\nemail ends with yahoo.com :", email.endswith('yahoo.com'))
print("email ends with gmail.com :", email.endswith('gmail.com'))

emails = ('abc123@gmail.com', 'xyz345@yahoo.com','pqr333@gmail.com',
          'asd555@hotmail.com', 'ghj456@yahoo.com','pql111@gmail.com')
print("\n-- emails ends with yahoo.com --")
for mail in emails:
    if mail.endswith('yahoo.com'):
        print(mail)

#replace()
print("\n-- replace a as @ in names")
for s in stu_names:
    print(s.lower().replace('a','@'))
    print(s.lower().replace('a','@',1))
        
#find()
name = 'manikanta'
print(name.find('a'))
print(name.find('an'))
print(name.find('ikon'))
          
#rfind()
print(name.rfind('a'))
print(name.rfind('an'))
print(name.rfind('ikon'))

#index()
print(name.index('a'))
print(name.index('an'))
          
#rindex()
print(name.rindex('a'))
print(name.rindex('an'))
print(name.rindex('ikon'))
