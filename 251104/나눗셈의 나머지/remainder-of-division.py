a,b = map(int,input().split())
lst = []
while a > 1:
    lst.append(a%b)
    a //= b

arr = [0]*b

for i in lst:
    arr[i] += 1

s = 0
for i in arr:
    s += i**2

print(s)