lst1 = list(input())
lst2 = list(input())

lst1.sort()
lst2.sort()

n = len(lst1)
cnt = 0

if len(lst2) != n:
    print('No')
else:
    for i in range(n):
        if lst1[i] != lst2[i]:
            print('No')
            break
        else:
            cnt += 1

if cnt ==n:
    print('Yes')