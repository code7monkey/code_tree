n = int(input())

# Please write your code here.
def isanghae(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return isanghae(n//3) + isanghae(n-1)

print(isanghae(n))