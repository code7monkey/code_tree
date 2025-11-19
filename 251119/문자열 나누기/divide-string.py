n = int(input())

lst = list(input().split())

tt = ''.join(lst)
m = len(tt)

i= 0

while i < m:
    print(tt[i:i+5])
    i += 5