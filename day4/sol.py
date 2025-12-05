i = open("input.in").read().splitlines()
count = 0

i = [list(col) for col in i]

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
    
    grid[pos[1]][pos[0]] = 'x'
    return True


row, col = 0, 0
while col < len(i):
    if col < 0:
        col = 0
    while row < len(i[col]):
        value = i[col][row]
        if checkNeighbours((row, col), i):
            count += 1
            row = -1
            col = 0
        row += 1
    row = 0
    col += 1

print(count)