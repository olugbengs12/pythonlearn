def computepay(hrs,r):
    if hrs > 40.0:
        p= ((40*r) +(hrs-40)* r *1.5)

    else:
        p =(hrs * r)

    return p
hrs = float(input("Enter worked hours: "))
r = float(input("Enter Pay rate per hour: "))
print (computepay(hrs,r))
