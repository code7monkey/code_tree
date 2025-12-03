n = int(input())

# Please write your code here.
def be_one(n):
    if n == 1:
        return 0 
    elif n % 2 == 1:
        return be_one(3*n+1) + 1
    else:
        return be_one(n//2) + 1
    
print(be_one(n))