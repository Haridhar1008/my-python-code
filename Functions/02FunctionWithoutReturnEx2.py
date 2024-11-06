#Function definition
def wish(user_name):
    msg = f"Hello {user_name}, Good evening"
    print(msg)

print(wish.__doc__)

#Function Calling 1 ( by passing static value)
wish('Pooja')

#Function Calling 2 ( by passing dynamic value)
uname = input("\nEnter user name : ")
wish(uname)
