filename = input("Please enter filename to open:")
try:
    fhandle = open(filename,"r")
except:
    print("Error opening file:", filename)
    exit()
spam = 0
spam_count = 0
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        spam += float(line[line.find(':')+1:])
        spam_count += 1

print("Average spam confidence:", spam/spam_count)
