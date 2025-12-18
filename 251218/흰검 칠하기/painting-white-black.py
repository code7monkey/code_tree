n = int(input())

OFFSET = 100000
SIZE = 200001

white = [0] * SIZE
black = [0] * SIZE
state = ['N'] * SIZE   # N: 안칠함, W: 흰, B: 검, G: 회색

cur = OFFSET

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        # 현재 포함해서 x칸을 왼쪽으로: [cur-x+1 .. cur]
        l = cur - (x - 1)
        r = cur
        for i in range(l, r + 1):
            if state[i] == 'G':
                continue
            white[i] += 1
            state[i] = 'W'
            if white[i] >= 2 and black[i] >= 2:
                state[i] = 'G'
        cur = l  # 마지막으로 칠한 타일 위치

    else:  # 'R'
        # 현재 포함해서 x칸을 오른쪽으로: [cur .. cur+x-1]
        l = cur
        r = cur + (x - 1)
        for i in range(l, r + 1):
            if state[i] == 'G':
                continue
            black[i] += 1
            state[i] = 'B'
            if white[i] >= 2 and black[i] >= 2:
                state[i] = 'G'
        cur = r  # 마지막으로 칠한 타일 위치

w_cnt = sum(1 for s in state if s == 'W')
b_cnt = sum(1 for s in state if s == 'B')
g_cnt = sum(1 for s in state if s == 'G')

print(w_cnt, b_cnt, g_cnt)


