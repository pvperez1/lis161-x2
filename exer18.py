filename = input("Please enter filename to open:")
try:
    fhandle = open(filename,"r")
except:
    print("Error opening file:", filename)
    exit()

emails = {}
for line in fhandle:
    if line.startswith("From "):
        email = line.strip().split()[1]
        emails[email] = emails.get(email,0) + 1

print(emails)
