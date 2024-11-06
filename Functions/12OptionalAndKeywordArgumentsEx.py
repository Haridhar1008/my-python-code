#Example for Optional Arguments and Keyword Arguments

#write a funtion to accept p, t and r claculate and print simple interest, tot amount(ptr/100)
def interest(amount, time = 12, rate = 0.6):
    si = (amount*time*rate)/100
    tot = amount + si
    print("\n---- Simple Interest ----\nPrincipal Amount : {}\nTime duration in months : {}\n\
Rate of interest in rupees : {}\nSimple Interest : {}\nTotal Amount : {}".format(amount, time,\
                                                                        rate, si, tot))

#function calling 1
interest(80000, 14, 1.5)

#function calling 2 ( Optional Arguments )
interest(80000, 14)
interest(80000)

#function calling 3
interest(rate=1, amount=50000)
