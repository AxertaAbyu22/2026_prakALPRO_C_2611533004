total = 0

while True:
    x = int(input("Enter a number: "))
    if x < 0:
        break
    if x == 0:
        continue
    print("Positive number:", x)
    total += x

print("Total:", total)