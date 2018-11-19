hrs = input("Enter Hours:")
h = float(hrs)
rate_hour = input("Enter rate:")
r = float(rate_hour)
if h <= 40:
    print (h * r)
else :
    print ((40 * r) + (h -40) * r * 1.5)
