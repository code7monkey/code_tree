size = 2001
offset = 1000

arr = [[0]*size for _ in range(size)]

x1, y1, x2, y2 = map(int, input().split())

for x in range(x1,x2):
    for y in range(y1,y2):
        arr[x + offset][y + offset] = 1

x1, y1, x2, y2 = map(int, input().split())

for x in range(x1,x2):
    for y in range(y1,y2):
        arr[x + offset][y + offset] = 0

min_x = size
max_x = -1
min_y = size
max_y = -1

for i in range(size):
    for j in range(size):
        if arr[i][j] == 1:
            if i < min_x: min_x = i
            if i > max_x: max_x = i
            if j < min_y: min_y = j
            if j > max_y: max_y = j

if max_x == -1:
    print(0)
else:
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    print(width * height)