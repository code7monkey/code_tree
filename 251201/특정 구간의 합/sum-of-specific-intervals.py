n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

for tup in queries:
    i = tup[0]-1
    j = tup[1]-1
    print(sum(arr[i:j+1]))

