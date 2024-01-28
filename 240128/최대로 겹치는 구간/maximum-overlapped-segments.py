n = int(input())
block = [0 for _ in range(200)]
command = [list(map(int, input().split())) for _ in range(n)]
for i,j in command:
    for k in range(100+i,100+j):
        block[k] += 1

print(max(block))