filename = input("Please enter filename to open:")
try:
    fhandle = open(filename,"r")
except:
    print("Error opening file:", filename)
    exit()

emails = {}
for line in fhandle:
    if line.startswith("From "):
        domain = line.strip().split()[1].split('@')[1]
        emails[domain] = emails.get(domain,0) + 1

print(emails)
