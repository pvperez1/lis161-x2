filename = input("Please enter filename to open:")
try:
    fhandle = open(filename,"r")
except:
    print("Error opening file:", filename)
    exit()

emails = {}
for line in fhandle:
    if line.startswith("From "):
        day = line.strip().split()[2]
        emails[day] = emails.get(day,0) + 1

print(emails)
