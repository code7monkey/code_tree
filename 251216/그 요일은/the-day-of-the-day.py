m1, d1, m2, d2 = map(int, input().split())
A = input()

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month , day = m1, d1
elapsed_time = 0

while True:
    if month == m2 and day == d2:
        break

    elapsed_time += 1
    day += 1

    if day > num_of_days[month]:
        month += 1
        day = 1

day_lst = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
x = day_lst.index(A)

print((elapsed_time - x)//7 +1)
