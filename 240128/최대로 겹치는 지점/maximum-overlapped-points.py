# 끝점에서 닿는 경우도 겹치는 것으로 봅니다.

n = int(input())
block = [0 for _ in range(101)]
for _ in range(n):
    a,b = map(int, input().split())
    for i in range(a,b+1):
        block[i] += 1

print(max(block))