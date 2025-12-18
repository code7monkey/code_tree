size = 201
offset = 100

arr = [[0]*size for _ in range(size)]

n = int(input())

for _ in range(n):
    x1, y1 = map(int, input().split())

    for x in range(x1,x1+8):
        for y in range(y1,y1+8):
            arr[x + offset][y + offset] = 1

ans = 0
for x in range(size):
    for y in range(size):
        ans += arr[x][y]

print(ans)
