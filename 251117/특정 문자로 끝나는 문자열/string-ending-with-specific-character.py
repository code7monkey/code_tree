lst = []

for _ in range(10):
    lst.append(input())

k = input()
cnt = 0

for st in lst:
    if st[-1] == k:
        print(st)
    else:
        cnt += 1

if cnt == 10:
    print('None')