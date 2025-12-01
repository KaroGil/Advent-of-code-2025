i = open("input.in").read().splitlines()

number = 50
count = 0
# Part 2
def checkBorder(num, count):
    if num > 99:
        count += 1
        return 0, count
    elif num < 0:
        return 99, count
    else:
        return num, count

for line in i:
    direction, step = line[0], int(line[1:])
    for _ in range(step):
        if direction == "R":
            number += 1
        elif direction == "L":
            number -= 1
        if number == 0:
            count += 1
        number, count = checkBorder(number, count)


print("count part 2: \t", count)


number = 50
count = 0

# Part 1
for line in i:
    direction, step = line[0], int(line[1:])

    if step > 99:
        step = step % 99
        count += step // 99

    number += step if direction == "R" else -step

    if number < 0:
        number = 100 + number
        count += 1
        
    elif number > 99:
        if number > 99:
            number = number - 100

    if number == 0:
        count += 1


print("count part 1: \t", count)
    