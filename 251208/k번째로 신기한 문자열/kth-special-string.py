n, k, t = input().split()
n, k = int(n), int(k)
lst = []

for _ in range(n):
    x = input()
    if x.startswith(t):
        lst.append(x)

lst.sort()
print(lst[2])