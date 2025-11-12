n, m = map(int, input().split())

'''
0,0 0,1 0,2 0,3 0,4 0,5
1,0 1,1 1,2 1,3 1,4 1,5
2,0 2,1 2,2 2,3
3,0 3,1 3,2
'''

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt = 0

for sums in range(n+m-1):
    i = max(0, sums - (m - 1))
    j = sums - i
    while i < n and i < sums+1:
        cnt += 1
        arr[i][j] = cnt 
        i += 1
        j -= 1

for lst in arr:
    for i in lst:
        print(i, end=' ')
    print()