M, D = map(int, input().split())

# Please write your code here.
def day_is(m,d):
    if m > 12 or d > 31:
        return 'No'
    elif m == 2:
        if d < 29:
            return 'Yes'
    elif m in [1,3,5,7,8,10,12]:
        if d < 32:
            return 'Yes'
    else:
        if d < 31:
            return 'Yes'
    return 'No'

print(day_is(M,D))