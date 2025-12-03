n = int(input())

# Please write your code here.
def namaji(n):
    if n == 1:
        return 2
    if n == 2:
        return 4

    return namaji(n-1)*namaji(n-2) % 100

print(namaji(n))