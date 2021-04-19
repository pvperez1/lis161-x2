def computepay(hours, rate):
    if hours > 40:
        pay = 40*rate + (hours-40)*1.5*rate
    else:
        pay = hours*rate
    return pay

try:
    hours = float(input("Enter Hours:"))
except:
    print("Please enter numerical value for Hours")
    exit()

try:
    rate = float(input("Enter Rate:"))
except:
    print("Please enter numerical value for Rate")
    exit()


#{:.2f} -> formatting to display 2 decimal places
print("Pay: {:.2f}".format(computepay(hours,rate)))
