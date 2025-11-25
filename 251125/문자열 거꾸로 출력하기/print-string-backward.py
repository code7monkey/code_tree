while True:
    s = input()
    if s == 'END':
        break
    else:   
        lst = list(s)
        n = len(lst)
        for i in range(n-1,-1,-1):
            print(lst[i],end='')
        print()