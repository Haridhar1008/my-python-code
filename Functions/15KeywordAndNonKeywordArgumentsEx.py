#Keyword Arguments
def student(*info, **marks):
    print("\ninfo = {}\ntype of info = {}".format(info, type(info)))
    print("\nmarks = {}\ntype of marks = {}".format(marks, \
                                                    type(marks)))
    if info:
        for i in info:
            print(i)
    else:
        print("info not available")
        
    if marks:
        for k,v in marks.items():
            print(f'{k} : {v}')
    else:
        print("marks not available")
    
#function calling 1
student(1001, 'Ravi', 'MPC', maths=88, physics=91, chemistry=79)

#function calling 2
student()
