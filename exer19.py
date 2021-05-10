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

max_count = None
max_email = None
for email,count in emails.items():
    if max_count is None:
        max_count = count
        max_email = email
    elif count > max_count:
        max_count = count
        max_email = email

print(max_email, max_count)
