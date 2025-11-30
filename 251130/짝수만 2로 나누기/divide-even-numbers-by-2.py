n = int(input())
lst = list(map(int, input().split()))

# Please write your code here.
def convert(lst):
    for i in range(n):
        if lst[i] % 2 ==0:
            lst[i] = lst[i]//2

convert(lst)

for i in lst:
    print(i,end=' ')
