def recursion(n):
    if n == 1:
        return 1
    return recursion(n-1) + n

n = int(input())
print(recursion(n))