n = int(input())
block = [0 for _ in range(2002)]
p = 1000
for _ in range(n):
    x,d = input().split()
    x = int(x)
    if d == 'L':
        for _ in range(x):
            block[p] += 1
            p -= 1
    else:
        for _ in range(x):
            block[p] += 1
            p += 1

print(len([i for i in block if i > 1]))