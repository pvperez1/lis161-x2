filename = input("Please enter filename to open:")
try:
    fhandle = open(filename,"r")
except:
    print("Error opening file:", filename)
    exit()

words = []
for line in fhandle:
    for word in line.split():
        if word not in words:
            words.append(word)

words.sort()
print(words)
