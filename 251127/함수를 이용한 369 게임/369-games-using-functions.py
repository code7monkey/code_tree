a, b = map(int, input().split())

def is_369(x):
    if x % 3 ==0:
        return True

    for i in str(x):
        if i in '369':
            return True
    
    return False

cnt = 0
for i in range(a,b+1):
    if is_369(i):
        cnt += 1
    
print(cnt)