a = 20  #global variable
def fun1():
    global a
    a = 45  #global variable
    print("Local variable a =", a)

def fun2():
    a = 55  #Local variable
    print("Local variable a =", a)

print("Global variable a =", a)
fun1()
print("Global variable a =", a)

fun2()
print("Global variable a =", a)
