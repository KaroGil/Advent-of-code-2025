battery_banks = open("input.in").read().splitlines()

sum_values = 0

for bank in battery_banks:
    powers = [(i, int(x)) for i, x in enumerate(bank)]
    print("Procent (%) done: " + str((battery_banks.index(bank) + 1) / len(battery_banks) * 100))
    max_val = -1
    # For the first digit i only have to search the first len(powers)-11 digits
    i1, m1 = max(powers[0:len(powers)-11], key=lambda x: x[1])

    # then the next biggest digit has to be after the first one but before len(powers)-10
    i2, m2 = max(powers[i1+1:len(powers)-10], key=lambda x: x[1])
    i3, m3 = max(powers[i2+1:len(powers)-9], key=lambda x: x[1])
    i4, m4 = max(powers[i3+1:len(powers)-8], key=lambda x: x[1])
    i5, m5 = max(powers[i4+1:len(powers)-7], key=lambda x: x[1])
    i6, m6 = max(powers[i5+1:len(powers)-6], key=lambda x: x[1])
    i7, m7 = max(powers[i6+1:len(powers)-5], key=lambda x: x[1])
    i8, m8 = max(powers[i7+1:len(powers)-4], key=lambda x: x[1])
    i9, m9 = max(powers[i8+1:len(powers)-3], key=lambda x: x[1])
    i10, m10 = max(powers[i9+1:len(powers)-2], key=lambda x: x[1])
    i11, m11 = max(powers[i10+1:len(powers)-1], key=lambda x: x[1])
    i12, m12 = max(powers[i11+1:len(powers)-0], key=lambda x: x[1])

    # now we have all 12 max values
    max_val = int(str(m1) + str(m2) + str(m3) + str(m4) + str(m5) + str(m6) + str(m7) + str(m8) + str(m9) + str(m10) + str(m11) + str(m12)) 
    print(max_val)
    sum_values += max_val

print("Sum: " + str(sum_values))