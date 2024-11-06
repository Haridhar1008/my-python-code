#function definition

#Write a function to accept a year and return is it leap year or not.
def isleapyear(year):
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        return True
    else:
        return False

#function calling 1
x = isleapyear(2000)
y = isleapyear(2022)
z = isleapyear(2024)
print(x,y,z,sep='\n')

#function calling 2
y = int(input("\nEnter a year(yyyy) : "))
r = isleapyear(y)
print(f"{y} is leap year : {r}")
