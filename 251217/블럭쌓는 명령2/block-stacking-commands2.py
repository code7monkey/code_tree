n, k = map(int, input().split())

# 1..n: 0
arr = [0 for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a-1,b):
        arr[i] += 1 

print(max(arr))