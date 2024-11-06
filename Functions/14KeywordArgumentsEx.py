#Keyword Arguments
def result(**marks):
    print("\nmarks = {}\ntype of marks = {}".format(marks, \
                                                    type(marks)))
    if marks:
        tot = sum(marks.values())
        avg = tot/len(marks)
        print("Total : {}\nAverage : {}".format(tot, avg))
    else:
        print("Marks not available")

#function calling 1
result(maths=88, physics=91, chemistry=79)

#function calling 2
result()
