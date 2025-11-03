lst = list(map(int,input().split()))

for i in range(10):
    if lst[i] % 3 ==0:
        t = i
        break
        
print(lst[t-1])