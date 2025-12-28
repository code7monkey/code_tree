n, m, k = map(int, input().split())
lst = [int(input()) for _ in range(m)]

pos = [0] * (n+1)
 
for i in lst:
    pos[i] += 1
    if pos[i] >= k:
        print(i)
        break