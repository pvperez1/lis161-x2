def computegrade(score):
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

score = input("Enter score:")

try:
    score = float(score)
except:
    print("Bad score")
    exit()

if not (0 <= score <= 1):
    print("Bad score")
    exit()

print(computegrade(score))
