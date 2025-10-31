n = int(input())
lst = list(map(float,input().split()))
m = sum(lst)/n
print(round(m,1))
if m >= 4.0:
    print('Perfect')
elif m >=3.0:
    print('Good')
else:
    print('Poor')