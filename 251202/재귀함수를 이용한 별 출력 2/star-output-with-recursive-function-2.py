n = int(input())

# Please write your code here.
def starr(n):
    if n ==0:
        return

    print('* '*n)
    starr(n-1)
    print('* '*n)

starr(n)