m1, d1, m2, d2 = map(int, input().split())

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

print(sum(month[m1:m2]) + d2 - d1 + 1)