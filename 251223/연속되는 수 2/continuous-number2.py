n = int(input())

lst = [int(input()) for _ in range(n)]
ans = []

cnt = 0
for i in range(n):
    cnt += 1
    if lst[i] != lst[i - 1]:
        ans.append(cnt)
        cnt = 0

if n == 1:
    print(1)
else:
    print(max(ans))
