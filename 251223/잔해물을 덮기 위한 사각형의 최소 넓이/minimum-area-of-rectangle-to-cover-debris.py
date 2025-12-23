size = 2001
offset = 1000

arr = [[0]*size for _ in range(size)]

x1, y1, x2, y2 = map(int, input().split())

for x in range(x1,x2+1):
    for y in range(y1,y2+1):
        arr[x + offset][y + offset] = 1

x1, y1, x2, y2 = map(int, input().split())

for x in range(x1,x2+1):
    for y in range(y1,y2+1):
        arr[x + offset][y + offset] = 0

ans = 0
for x in range(size):
    for y in range(size):
        ans += arr[x][y]

print(ans)