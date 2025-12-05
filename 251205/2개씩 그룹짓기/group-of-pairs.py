n = int(input())
lst = list(map(int, input().split()))
lst2 = []
# Please write your code here.
lst.sort()
for i in range(n):
    lst2.append(lst[i]+lst[2*n-1-i])

print(max(lst2))