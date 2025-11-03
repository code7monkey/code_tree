odd = 0
even = 0

lst = list(map(int,input().split()))

for i in range(0,10,2):
    odd += lst[i]

for i in range(1,10,2):
    even += lst[i]

print(abs(odd-even))