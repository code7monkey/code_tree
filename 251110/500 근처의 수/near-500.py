lst = list(map(int,input().split()))

a = []
b = []

for i in lst:
    if i > 500:
        a.append(i)
    elif i < 500:
        b.append(i)

print(max(b), min(a),sep=' ')