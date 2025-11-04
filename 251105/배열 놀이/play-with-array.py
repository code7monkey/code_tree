n, q = map(int,input().split())

lst = list(map(int,input().split()))

for _ in range(q):
    arr = list(map(int,input().split()))
    if arr[0] == 1:
        a = arr[1]
        print(lst[a-1])
    elif arr[0] == 2:
        b = arr[1]
        idx = 0
        for i in range(n):
            if lst[i] == b:
                idx = i+1
                break
        print(idx)
    else:
        s = arr[1]
        e = arr[2]
        for i in range(s-1,e):
            print(lst[i],end=' ')
        print()