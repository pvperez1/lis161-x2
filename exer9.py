sum = 0
count = 0
ave = None

while True:
    num = input("Enter a number:")
    if num == "done":
        break
    try:
        num = float(num)
    except:
        print("Invalid input")
        continue
    sum += num
    count += 1

if count == 0:
    print(sum, count, ave)
else:
    print(sum, count, sum/count)
