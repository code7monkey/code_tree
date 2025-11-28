a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def calculate(x,n,m):
    if x == '+':
        print(f'{n} + {m} = {n+m}')
    elif x == '-':
        print(f'{n} - {m} = {n-m}')
    elif x =='/':
        print(f'{n} / {m} = {n/m}')
    elif x =='*':
        print(f'{n} * {m} = {n*m}')
    else:
        print('False')

calculate(o,a,c)
