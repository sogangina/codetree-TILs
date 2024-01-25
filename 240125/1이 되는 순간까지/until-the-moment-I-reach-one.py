def recursion(n, k):
    if n == 1:
        return k
    if n%2 == 0:
        return recursion(n//2, k+1)
    if n%2:
        return recursion(n//3, k+1)

n = int(input())
print(recursion(n,0))