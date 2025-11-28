a, b = map(int, input().split())

# Please write your code here.
def sosu(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    
    return True

def even(x):
    ss = x // 10 + x % 10
    if ss % 2 ==0:
        return True
    
    return False

cnt = 0

for i in range(a,b+1):
    if sosu(i) and even(i):
        cnt += 1
    
print(cnt)