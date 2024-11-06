#function definition
'''write a function to accept purchase amount and discount percentage
and return discount amount, bill amount'''

def find_discount(amt, dis):
    d_amt = amt * dis / 100
    b_amt = amt - d_amt
    return d_amt, b_amt

#function calling 1
x,y = find_discount(2950, 8.5)
print("Discount amount :", x)
print("Bill Amount :", y)

#function calling 2
a = float(input("\nEnter purchase amount : "))
d = float(input("Enter discount percentage : "))
p,q = find_discount(a, d)
print("Discount amount :", p)
print("Bill Amount :", q)
