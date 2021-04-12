hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

#{:.2f} -> formatting to display 2 decimal places
print("Pay: {:.2f}".format(rate*hours))
