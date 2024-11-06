'''A company decided to give bonus to employee according to following
criteria:
Time period of Service        Bonus
More than 10 years             11%
>=6 and <=10                   8%
Less than 6 years              5%

accept salary and years of service from user and print
the net bonus amount.'''

exp = int(input("Enter years of service : "))
sal = float(input("Enter employee salary : "))

if exp > 10:
    bonus = 11
elif exp >= 6 and exp <= 10:
    bonus = 8
else:
    bonus = 5
print(f"\nHello, you got {bonus}% bonus")

b_amt = sal * bonus / 100
print("Bonus amount : {:.2f}".format(b_amt))
