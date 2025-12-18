n = int(input())

offset = 100000
size = 200001

state = ['N'] * size

cur = offset

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        # 현재 포함해서 x칸 왼쪽으로
        l = cur - (x-1)
        r = cur 
        for i in range(l, r+1):
            state[i] = 'W'
        cur = l

    else:
        l = cur
        r = cur + (x-1)
        for i in range(l,r+1):
            state[i] = 'B'
        cur = r

w_cnt = sum(1 for s in state if s =='W')
b_cnt = sum(1 for s in state if s =='B')

print(w_cnt, b_cnt)