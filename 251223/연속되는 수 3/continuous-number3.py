n = int(input())

lst = [int(input()) for _ in range(n)]

min_idx = 0
ans = []

for i in range(n):
    if lst[i] * lst[i-1] < 0 or i == n-1:
        ans.append(i - min_idx)
        min_idx = i

print(max(ans))

