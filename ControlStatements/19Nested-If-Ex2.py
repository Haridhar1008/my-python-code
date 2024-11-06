'''Write a program to accept three subject marks from user i.e. maths,
physics and chemistry from user, and Calculate total,  percentage
and grade according to following:

Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Fail '''

m = int(input("Enter maths marks : "))
p = int(input("Enter physics marks : "))
c = int(input("Enter chemistry marks : "))

tot = m + p + c
per = tot * 100 / 300
res = ''

if m >= 40 and p >= 40 and c >= 40:
    if per >= 90:
        res = 'Grade A'
    elif per >= 80:
        res = 'Grade B'
    elif per >= 70:
        res = 'Grade C'
    elif per >= 60:
        res = 'Grade D'
    else:
        res = 'Grade E'
else:
    res = 'Fail'

print("\n---- Result ----\nTotal : {}\nPercentage : {:.2f}\n\
Result : {}".format(tot, per, res))
