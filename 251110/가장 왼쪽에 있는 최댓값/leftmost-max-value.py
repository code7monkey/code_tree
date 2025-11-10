n = int(input())
lst = list(map(int, input().split()))

idx = 0 
m = min(lst) -1

while True:
    idx = 0
    m = min(lst) -1
    for i in range(n):
        if lst[i] > m:
            idx = i + 1
            m = lst[i]
    print(idx, end=' ')
    n = idx -1
    if idx == 1:
        break