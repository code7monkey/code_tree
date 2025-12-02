n = int(input())

# Please write your code here.
def staarrr(n):
    if n == 0:
        return

    staarrr(n-1)
    print('*'*n)

staarrr(n)