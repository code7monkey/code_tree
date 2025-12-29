n = int(input())

x,y = 0,0
# 0: 동, 1: 남, 2: 서, 3: 북
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

def convert_dir_num(x):
    if x == 'E':
        return 0
    elif x == 'S':
        return 1
    elif x =='W':
        return 2
    else:
        return 3

for _ in range(n):
    a, b = input().split()
    b = int(b)
    a = convert_dir_num(a)
    x = x + b*dx[a]
    y = y + b*dy[a]

print(x,y)