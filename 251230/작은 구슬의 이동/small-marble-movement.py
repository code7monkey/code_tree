N, T = map(int, input().split())
R, C, D = input().split()

# x,y = R(행), C(열)
x = int(R) - 1
y = int(C) - 1

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

dir_num = mapper[D]

def in_range(a, b):
    return 0 <= a and a < N and 0 <= b and b < N

times = 0

while times < T:
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny):  # check whether position is out of grid
        dir_num = 3 - dir_num # change direction
        times += 1
        continue

    # move
    x, y = nx, ny
    times += 1

print(x+1 ,y+1)
