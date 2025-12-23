n = int(input())

lst = [int(input()) for _ in range(n)]
ans = []

cnt = 0
for i in range(n):
    cnt += 1
    if i ==0:
        continue
    elif lst[i] != lst[i - 1]:
        ans.append(cnt)
        cnt = 0

print(max(ans))
