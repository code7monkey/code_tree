s, q = input().split()
q = int(q)
n = len(s)

# 1은 왼쪽 밀기
# 2는 오른쪽 밀기
# 3은 좌우반전
for _ in range(q):
    i = int(input())
    if i ==1:
        s = s[1:] + s[0]
        print(s)
    elif i ==2:
        s = s[-1] + s[:-1]
        print(s)
    else:
        t = ''
        for i in range(n-1,-1,-1):
            t += s[i]
        s = t
        print(s)
            