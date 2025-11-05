n = int(input())
lst = list(map(int, input().split()))

# Please write your code here.
a = min(lst)
cnt = lst.count(a)
print(a,cnt,sep=' ')