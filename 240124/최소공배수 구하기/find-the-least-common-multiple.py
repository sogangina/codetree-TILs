n,m = map(int, input().split())

for k in range(m,n*m+1,m):
    if k % n == 0:
        print(k)
        break