n = int(input())

# Please write your code here.
def sqq(n):
    if n < 10:
        return n**2

    return sqq(n//10) + (n%10)**2

print(sqq(n))