y = int(input())

def younun(x):
    if x % 4 ==0:
        if x % 100 ==0 and x % 400 != 0:
            return 'false'
        else:
            return 'true'
    return 'false'

print(younun(y))