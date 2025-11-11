lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))

print(sum(lst1)/4, end=' ')
print(sum(lst2)/4)

for i in range(4):
    print((lst1[i]+lst2[i])/2,end=' ')
print()

print((sum(lst1)+sum(lst2))/8)