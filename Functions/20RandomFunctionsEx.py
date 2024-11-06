import random

x = [1,2,3,4,5,6]
y = ('Apple','Mango','Grapes', 'Banana','Orange')
z = 'python'
books = [[101,'C'], [102,'C++'],[103,'Python'],[104,'.Net'],
         [105,'Java'],[106,'Oracle']]

#choice()
print("range of 100 : ", random.choice(range(100)))
print("From list   : ", random.choice(x))
print("From tuple  : ", random.choice(y))
print("From string : ", random.choice(z))
print("From nested list : ", random.choice(books))

#randrange()
print("\nrandrange of 1 to 100 odd : ",\
      random.randrange(1, 101, 2))
print("randrange of 2 to 100 even : ",\
      random.randrange(2, 101, 2))
print("randrange of 0 to 100 : ", random.randrange(100))

#random()
print("\nrandon of 0.0 to 1.0 : ", random.random())

#uniform()
print("\nuniform of 5.5 to 10.9 : ", random.uniform(5.5, 10.9))

#shuffle()
print("\nBefore shuffle books : ", books)
random.shuffle(books)
print("\nAfter shuffle books : ", books)

#Password generation
uname = input("Enter user name : ")
ch1 = random.choice(uname).upper()
ch2 = random.choice(uname).lower()
p =  random.randrange(1000,10000)

pwd = ch2 + str(p) + ch1
print("Your password : ", pwd)

