i = open("input.in").read().splitlines()
count = 0

def checkNeighbours(pos, grid):
    count_n = 0
    current = grid[pos[1]][pos[0]]
    if current != '@':
        return False
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    for d in directions:
        new_x = pos[0] + d[0]
        new_y = pos[1] + d[1]
        if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
            if grid[new_y][new_x] == '@':
                count_n += 1
    if count_n >= 4:
        return False
    return True

for col in range(len(i)):
    for row in range(len(i[col])):
        if checkNeighbours((row, col), i):
            count += 1


print(count)