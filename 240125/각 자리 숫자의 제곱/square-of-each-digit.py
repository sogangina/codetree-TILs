def recursion(n):
    if n < 10:
        return n**2
    return recursion(n//10) + recursion(n%10)

n = int(input())
print(recursion(n))