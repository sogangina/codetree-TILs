m1, d1, m2, d2 = map(int, input().split())

months = [31,28,31,30,31,30,31,31,30,31,30,31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

elapsed1 = sum(months[:m1]) + d1
elapsed2 = sum(months[:m2]) + d2

print(days[(elapsed2 - elapsed1) % 7])