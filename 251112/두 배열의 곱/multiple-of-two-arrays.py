arr1 = []
arr2 = []

for _ in range(3):
    lst = list(map(int,input().split()))
    arr1.append(lst)
blank = input()
for _ in range(3):
    lst = list(map(int,input().split()))
    arr2.append(lst)

for i in range(3):
    for j in range(3):
        print(arr1[i][j] * arr2[i][j], end=' ')
    print()