def minimum(a,b,c):
    c1 = a if a<b else b
    c2 = b if b<c1 else c1
    c3 = c if c<c2 else c2
    return c3

a,b,c = map(int, input().split())
print(minimum(a,b,c))