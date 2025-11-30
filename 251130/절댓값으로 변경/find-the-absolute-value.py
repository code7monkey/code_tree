n = int(input())
arr = list(map(int, input().split()))

def absss(lst):
    for i in range(n):
        lst[i] = abs(lst[i])

absss(arr)

for i in arr:
    print(i,end=' ')