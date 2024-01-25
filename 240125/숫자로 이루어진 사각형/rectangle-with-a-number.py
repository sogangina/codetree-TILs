def function(n):
    placeholder = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            placeholder[i][j] = (i*n + j) % 9 + 1
        print(*placeholder[i])

n = int(input())
function(n)