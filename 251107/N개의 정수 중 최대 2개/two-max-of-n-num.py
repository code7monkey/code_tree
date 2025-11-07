n = int(input())
lst = list(map(int, input().split()))

a = max(lst)
b = min(lst)

max_val= b
if lst.count(a) >= 2:
    print(a,a,sep=' ')
else:
    for i in lst:
        if i < a:
            if max_val < i:
                max_val = i
    print(a,max_val,sep=' ')