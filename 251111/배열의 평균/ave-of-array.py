lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))

print(round(sum(lst1)/4,1), end=' ')
print(round(sum(lst2)/4,1))

for i in range(4):
    print(round((lst1[i]+lst2[i])/2,1),end=' ')
print()

print(round((sum(lst1)+sum(lst2))/8,1))