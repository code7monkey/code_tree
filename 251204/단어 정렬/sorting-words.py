n = int(input())
lst = [input() for _ in range(n)]

# Please write your code here.
lst.sort()
for i in lst:
    print(i)