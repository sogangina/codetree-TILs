n = int(input())
number = [int(input()) > 0 for _ in range(n)]

ans, cnt = 0,0
for i in range(n):
    if i > 0 and number[i] == number[i-1]:
        ans += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans, cnt)
print(ans)