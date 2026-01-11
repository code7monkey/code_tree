n, t = map(int, input().split())
R, C, D = input().split()

# x가 행, y가 열
# 나중에 다시 1 더해줘서 출력
x = int(R) - 1
y = int(C) - 1

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def in_ran(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def conv_dir(p):
    if p == 'R':
        return 0
    elif p == 'D':
        return 1
    elif p == 'U':
        return 2
    else:
        return 3

dir_num = conv_dir(D)

# nx, ny는 미리보기 느낌, dir_num을 바꾼 뒤 x,y에 반영 해야함
for _ in range(t):
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    
    # 벽 부딫히는거
    if not in_ran(nx,ny):
        dir_num = 3 - dir_num
    # 이동
    else:
        x, y = nx, ny

print(x+1, y+1)