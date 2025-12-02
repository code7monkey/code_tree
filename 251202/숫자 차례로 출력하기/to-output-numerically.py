n = int(input())
k = n+1 

# Please write your code here.
def sssstar(n):
    if n ==0:
        print()
        return
    
    print(k-n, end=' ')
    sssstar(n-1)
    print(k-n, end=' ')

sssstar(n)