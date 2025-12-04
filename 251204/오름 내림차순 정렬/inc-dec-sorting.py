n = int(input())
lst = list(map(int, input().split()))

# Please write your code here.
lst.sort()
print(*lst)
lst = lst[::-1]
print(*lst)