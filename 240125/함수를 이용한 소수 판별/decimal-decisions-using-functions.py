def isprime(n):
    return n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

a,b = map(int, input().split())

print(sum([i for i in range(a,b+1) if isprime(i)]))