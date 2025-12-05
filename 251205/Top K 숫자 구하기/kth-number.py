n, k = map(int, input().split())
lst = list(map(int, input().split()))

# Please write your code here.
lst.sort()
print(lst[k-1])