with open('day3.txt', 'r') as file:
    matrix = file.read().splitlines()

rows = len(matrix)
columns = len(matrix[0])

directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
    [-1, -1],
    [1, 1],
    [1, -1],
    [-1, 1],
    ]

numbers = "0123456789"
visited = set()

def get_number(i, j):
    if i >= rows or j >= columns or i < 0 or j < 0 or (i, j) in visited:
        return 0
    if matrix[i][j] not in numbers:
        return 0
    digit = matrix[i][j]
    left = j - 1
    right = j + 1
    #left + digit + right
    while left >= 0:
        if matrix[i][left] not in numbers:
            break
        digit = matrix[i][left] + digit # ('1' + '2' = 12)
        visited.add((i, left))
        left -= 1

    while right < columns:
        if matrix[i][right] not in numbers:
            break
        digit = digit + matrix[i][right]
        visited.add((i, right))
        right += 1
    
    return int(digit) 


total = 0
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == '*':
            all_values = [get_number(i + dx, j + dy) for dx, dy in directions]
            all_values = [value for value in all_values if value > 0]
            if len(all_values) == 2:
                total += all_values[0]*all_values[1]
            # print(all_values)
        #print(i, j)
        #print(adjacent_values)

print(total)