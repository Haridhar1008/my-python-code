'''A shop will give discount of 11% if the cost of purchased quantity
is more than 1000 otherwise 5%.

Accept purchased amount from user and find discount percentage,
discount amount and bill amount '''

amt = float(input("Enter purchase amount : "))

if amt > 1000:
    dis = 11
else:
    dis = 5
print("Hello, you got {}% discount".format(dis))

dis_amt = amt * dis/100
print("Discount Amount :", dis_amt)

bill_amt = amt - dis_amt
print("Bill Amount :", bill_amt)
