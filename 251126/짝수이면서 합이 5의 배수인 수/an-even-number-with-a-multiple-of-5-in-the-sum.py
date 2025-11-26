x = int(input())

def eve(n):
    chk = 'No'
    if n % 2 ==0 and (n//10+n%5) % 5 ==0:
        chk = 'Yes'
    return chk

print(eve(x))