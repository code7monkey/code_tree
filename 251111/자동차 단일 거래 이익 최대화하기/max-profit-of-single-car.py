n = int(input())
lst = list(map(int, input().split()))

price = []

for i in range(n-1,0,-1):
    for j in range(i-1,-1, -1):
        t = lst[i] - lst[j]
        if t > 0:
            price.append(t)

if len(price) > 0:
    print(max(price))
else:
    print(0)