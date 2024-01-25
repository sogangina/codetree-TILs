n = int(input())
number = list(map(int, input().split()))

for i in range(n):
    if i%2:
        continue
    part = number[:i+1]
    print(sorted(part)[(i+1)//2], end=' ')