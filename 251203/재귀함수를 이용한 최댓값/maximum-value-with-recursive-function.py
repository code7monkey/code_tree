n = int(input())
lst = list(map(int, input().split()))

# Please write your code here.
def find_max(n):

    if n == 1:
        return(lst[0])

    return max(find_max(n-1), lst[n-1])

print(find_max(n))
