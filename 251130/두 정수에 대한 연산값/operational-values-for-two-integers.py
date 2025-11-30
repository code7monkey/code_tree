a, b = map(int, input().split())

# Please write your code here.
def cal(x,y):
    if x > y:
        return x+25, 2*y
    return 2*x, y+25

a,b = cal(a,b)

print(a, b)