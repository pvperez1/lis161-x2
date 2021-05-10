filename = input("Please enter filename to open:")
try:
    fhandle = open(filename,"r")
except:
    print("Error opening file:", filename)
    exit()

emails = []
for line in fhandle:
    if line.startswith("From "):
        emails.append(line.strip().split()[1])

for email in emails:
    print(email)
print("There were {} lines in the file with From as the first word".format(len(emails)))
