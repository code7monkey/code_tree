offset = 1000
size = 2001

arr = [[0] * size for _ in range(size)]

for i in range(3):
    x1, y1, x2, y2 = map(int,input().split())
    if i ==2: 
        for x in range(x1,x2):
            for y in range(y1,y2):
                arr[x + offset][y + offset] = 0
    else: 
        for x in range(x1,x2):
            for y in range(y1,y2):
                arr[x + offset][y + offset] = 1

ans = 0
for x in range(size):
    for y in range(size):
        ans += arr[x][y]

print(ans)