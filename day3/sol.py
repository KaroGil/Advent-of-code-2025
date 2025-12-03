battery_banks = open("input.in").read().splitlines()

sum_values = 0
joltage_length = 12

for bank in battery_banks:
    powers = [(i, int(x)) for i, x in enumerate(bank)]
    l = len(powers)
    count = ""
    prev_ind = -1
    for i in range(joltage_length):
        prev_ind, value = max(powers[prev_ind + 1:l- (joltage_length -i - 1)], key=lambda x: x[1])
        count += str(value)

    max_val = int(count)
    sum_values += max_val

print("Sum: " + str(sum_values))