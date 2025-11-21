s,q = input().split()
q = int(q)
lst = list(s)
n = len(s)

for _ in range(q):
    a,b,c = input().split()
    if a =='1':
        a,b,c = int(a),int(b),int(c)
        lst[b-1], lst[c-1] = lst[c-1], lst[b-1]
    else:
        for i in range(n):
            if lst[i] == b:
                lst[i] = c

    for i in range(n):
        print(lst[i],end='')
    print()
