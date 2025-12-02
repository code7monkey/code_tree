n = int(input())
cnt = 0

# Please write your code here.
def become_one(n):
    global cnt 
    if n == 1:
        return
    elif n % 2 ==0:
        cnt += 1
        return become_one(n//2)
    else:
        cnt += 1
        return become_one(n//3)

become_one(n)
print(cnt)