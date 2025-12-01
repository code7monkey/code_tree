n = int(input())

# Please write your code here.
def helllo(n):
    if n == 0:
        return

    helllo(n-1)
    print("HelloWorld")

helllo(4)