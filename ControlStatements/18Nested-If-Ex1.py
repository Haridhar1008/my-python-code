'''Take a tuple with user id and password like, user=('pooja','p1001'),
then accept userid and password from user and check the given userid
and password are match with existing userid and password or not.'''

user = ('pooja', 'p1001')

uid = input("Enter user id : ")
pwd = input("Enter password : ")

#by using nested if
if uid == user[0]:
    if pwd == user[1]:
        print(f"Hello {uid}, You are authorized user")
    else:
        print("Invalid password")
else:
    print("Invalid user id")

#by using if - else
if uid == user[0] and pwd == user[1]:
    print(f"Hello {uid}, You are authorized user")
else:
    print("Invalid user id / password")


