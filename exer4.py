hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

if hours > 40:
    pay = 40*rate + (hours-40)*1.5*rate
else:
    pay = hours*rate

#{:.2f} -> formatting to display 2 decimal places
print("Pay: {:.2f}".format(pay))
