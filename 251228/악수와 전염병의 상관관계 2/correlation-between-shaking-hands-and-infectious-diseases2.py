N, K, P, T = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(T)]

# 인덱스 0 ~ n-1 == 1 ~ n
pos = [0] * N

# 첫번째 감염자
pos[P-1] = 1

# t를 기준으로 오름차순
lst.sort(key= lambda x: x[0])

for i in range(K):

    if pos[lst[i][1]-1] == 1:
        pos[lst[i][2]-1] = 1

    elif pos[lst[i][2]-1] == 1:
        pos[lst[i][1]-1] = 1
    
print(*pos,sep='')
