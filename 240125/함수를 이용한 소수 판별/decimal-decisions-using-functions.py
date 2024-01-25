def isprime(n):
    result = True
    root = int(n**0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            result = False
            break
    return result

a,b = map(int, input().split())

print(sum([i for i in range(a,b+1) if isprime(i)]))