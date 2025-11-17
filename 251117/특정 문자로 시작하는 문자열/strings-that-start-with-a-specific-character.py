n = int(input())

lst = []

for _ in range(n):
    lst.append(input())

k = input()

cnt = 0
ll = 0

for st in lst:
    if k in st:
        cnt += 1
        ll += len(st)

print(cnt,end=' ')
print(f'{ll/cnt:.2f}')