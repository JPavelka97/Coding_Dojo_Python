count = 0
while count <= 150:
    print(count)
    count += 1

count = 0
while count <= 1000:
    print(count)
    count += 5

count = 0
while count <= 100:
    if count % 10 == 0:
        print("Coding Dojo")
        count += 1
    elif count % 5 == 0:
        print("Coding")
        count += 1
    else:
        print(count)
        count += 1

count = 0
sum = 0
while count <= 500000:
    if count % 2 == 0:
        count += 1
        continue
    else:
        sum += count
        count += 1
print(sum)

count = 2018
while count > 0:
    print(count)
    count -= 4

lowNum = 2
highNum = 30
mult = 3
while lowNum <= highNum:
    if lowNum % mult == 0:
        print(lowNum)
        lowNum += 1
    else:
        lowNum += 1
