a, b, c = map(int, input().split())

lst = list(str(a*b*c))
n = len(lst)
# Please write your code here.
def muullti(n):

    if n == 1:
        return int(lst[0])

    return muullti(n-1)+int(lst[n-1])

print(muullti(n))