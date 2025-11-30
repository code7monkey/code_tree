a, b = map(int, input().split())

# Please write your code here.
def nummm(x,y):
    if x > y:
        return 2*x, y+10
    return x+10, 2*y

a,b = nummm(a,b)
print(a, b)