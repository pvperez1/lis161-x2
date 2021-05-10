filename = input("Please enter filename to open:")
if filename == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()

try:
    fhandle = open(filename,"r")
except:
    print("Error opening file:", filename)
    exit()

sub_count = 0
for line in fhandle:
    if line.startswith('Subject:'):
        sub_count += 1

print("There were",sub_count,"subject lines in",filename)
