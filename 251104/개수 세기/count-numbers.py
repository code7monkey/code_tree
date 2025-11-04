n, m =map(int,input().split())
lst = list(map(int,input().split()))
idx = -1
cnt = 0

for i in range(n):
    if lst[i] == m:
        cnt += 1
        
print(cnt)