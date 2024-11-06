#Write a function to accept 3 subject marks and return tot,avg and res.

#function definition
def result(marks1, marks2, marks3):
    tot = marks1 + marks2 + marks3
    avg = tot / 3
    res = ''
    if marks1 >= 35 and marks2 >= 35 and  marks3 >= 35:
        if avg >= 80:
            res = 'First Class'
        elif avg >= 60:
            res = "Second Class"
        else:
            res = 'Third Class'
    else:
        res = 'Fail'
    return tot, avg, res
        
#function calling 1
x,y,z = result(91, 84, 88)
print("Total : {}\nAverage : {:.2f}\nResult : {}".format(x,y,z))

#function calling 2
m1 = int(input("\nEnter 1st subject marks : "))
m2 = int(input("Enter 2nd subject marks : "))
m3 = int(input("Enter 3rd subject marks : "))
p,q,r = result(m1, m2, m3)
print("Total : {}\nAverage : {:.2f}\nResult : {}".format(p,q,r))
