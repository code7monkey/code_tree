n =int(input())
lst = list(map(int,input().split()))

arr = [0]*9
for i in lst:
    arr[i-1] += 1

for i in arr:
    print(i)