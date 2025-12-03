i = open("input.in").read()

sumOfInvalidIds = 0

ranges = i.split(",")

def check_invalid(id):
    i = (id+id).find(id, 1, -1)
    return False if i == -1 else True

for r in ranges:
    first_id, last_id = r.split("-")

    for id_num in range(int(first_id), int(last_id)+1):
        id_str = str(id_num)
        if check_invalid(id_str):
            sumOfInvalidIds += id_num


print(sumOfInvalidIds)
    