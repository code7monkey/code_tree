n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x,y = 0,0

# 방향전환
def conv_dir(x):
    if x == 'E':
        return 0
    elif x == 'S':
        return 1
    elif x == 'W':
        return 2
    else:
        return 3
    
for _ in range(n):
    dir, ran = input().split()
    ran = int(ran)
    dir = conv_dir(dir)
    x, y = x + ran*dx[dir], y + ran*dy[dir]

print(x, y)