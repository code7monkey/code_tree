n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def chk_cont(a,b,n1,n2):
    for i in range(n1-n2+1):
        if a[i:i+n2] == b:
            return 'Yes'
    return 'No'
    
print(chk_cont(a,b,n1,n2))