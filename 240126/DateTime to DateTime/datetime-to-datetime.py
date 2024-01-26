a,b,c = map(int, input().split())

if a == 11:
    if b < 11 or (b == 11 and c < 11):
        print(-1)
else:
    offset = 11 * 60 + 11
    now = (a - 11) * 60 * 24 + b * 60 + c
    print(now - offset)