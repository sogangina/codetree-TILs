a,b,c = map(int, input().split())

offset = 11 * 60 + 11
now = (a - 11) * 60 * 24 + b * 60 + c
print(max((now - offset, -1)))