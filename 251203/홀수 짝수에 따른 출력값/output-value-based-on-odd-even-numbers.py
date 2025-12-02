n = int(input())

# n -> n-2
def sssuuumm(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return sssuuumm(n-2) + n 

print(sssuuumm(n))

    