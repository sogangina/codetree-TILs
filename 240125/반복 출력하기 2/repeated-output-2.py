def recursion(n):
    if n == 0:
        return
    recursion(n-1)
    print("HelloWorld")

n = int(input())

recursion(n)