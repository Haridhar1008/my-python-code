#Non Keyword Arguments
def result(*marks):
    print("\nmarks = {}\ntype of marks = {}".format(marks, type(marks)))
    if marks:
        tot = sum(marks)
        avg = tot/len(marks)
        print("Total :", tot)
        print("Average :", avg)
    else:
        print("Marks not available")


#function calling 1
result(88, 91, 75, 82)

#function calling 2
result()
