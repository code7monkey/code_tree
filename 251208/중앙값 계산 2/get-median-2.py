n = int(input())
lst = list(map(int, input().split()))

# Please write your code here.
lst2 = []
for i in range(n):
    lst2.append(lst[i])
    lst2.sort()
    if i % 2 ==0:
        print(lst2[(i+2)//2-1],end=' ')