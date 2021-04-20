sum = 0
count = 0
max = None
min = None

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
    if min is None or num < min:
        min = num
    if max is None or num > max:
        max = num


print(sum, count, min, max)
