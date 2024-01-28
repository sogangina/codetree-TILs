n = int(input())
number = [int(input()) for _ in range(n)]
cnt = 1
maximum = 1
for i in range(1,n):
    if number[i-1] == number[i]:
        cnt += 1
    else:
        maximum = max(cnt, maximum)
        cnt = 1
    maximum = max(cnt, maximum)
print(maximum)