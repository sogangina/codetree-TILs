def recursion(n):
    if n == 0:
        return
    recursion(n-1)
    print('*'*n)

n = int(input())
recursion(n)