n = int(input())
lst = list(map(int, input().split()))

# Please write your code here.
def gcd(x,y):
    while y:
        x,y = y, x%y
    return x

def lcm(x,y):
    return (x*y) // gcd(x,y)

def minnn(n):

    if n==1:
        return lst[0]

    return lcm(minnn(n-1), lst[n-1] )

print(minnn(n))