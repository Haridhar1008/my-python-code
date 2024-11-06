'''A student will not be allowed to sit in exam if his/her attendance
is less than 75%.

Take following input from user
    Number of classes held
    Number of classes attended.
    And print attendance percentage and check Is student is allowed
    to sit in exam or not.'''

tot_cls = int(input("Enter number of classes held : "))
att_cls = int(input("Enter number of classes attended : "))

att_per = att_cls * 100 / tot_cls
print("\nAttendance Percentage : {:.2f}".format(att_per))

if att_per < 75:
    print("Student is not allowed to sit in exam")
else:
    print("Student is allowed to sit in exam")
