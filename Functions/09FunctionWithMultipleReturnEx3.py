#write a function to accept list of marks and return to, avg and res

#function definition
def result(marks = []):
    if bool(marks):
        tot = sum(marks)
        avg = tot/len(marks)
        res = ''
        if min(marks) >= 35:
            if avg >= 80:
                res = 'Grade A'
            elif avg >= 60:
                res = 'Grade B'
            else:
                res = 'Grade C'
        else:
            res = 'Fail'
        return tot, avg, res
    else:
        return 0,0.0,None
            
#function calling 1
x,y,z = result([88,91,76,77])
print("Total : {}\nAverage : {:.2f}\nResult : {}".format(x,y,z))

#function calling 2
n = int(input("\nEnter no of subjects : "))
m = []
for i in range(n):
    j = int(input(f"Enter marks {i+1}: "))
    m.append(j)

p,q,r = result(m)
print("Total : {}\nAverage : {:.2f}\nResult : {}".format(p,q,r))
