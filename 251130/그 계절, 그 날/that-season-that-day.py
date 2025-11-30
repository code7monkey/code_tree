Y, M, D = map(int, input().split())

# Please write your code here.
def is_yoon(y):
    if y%4 ==0:
        if y%100 ==0 and y%400 !=0:
            return False
        else:
            return True
    return False

def day_is(y,m,d):
    if is_yoon(y):
        if m == 2:
            if d < 30:
                return 'Yes'
        elif m in [1,3,5,7,8,10,12]:
            if d < 32:
                return 'Yes'
        else:
            if d < 31:
                return 'Yes'
    else:
        if m == 2:
            if d < 29:
                return 'Yes'
        elif m in [1,3,5,7,8,10,12]:
            if d < 32:
                return 'Yes'
        else:
            if d < 31:
                return 'Yes'
    return 'No'

def season(y,m,d):
    if day_is(y,m,d) == 'Yes':
        if m in [3,4,5]:
            return 'Spring'
        elif m in [6,7,8]:
            return 'Summer'
        elif m in [9,10,11]:
            return 'Fall'
        else:
            return 'Winter'
    return -1

print(season(Y,M,D))