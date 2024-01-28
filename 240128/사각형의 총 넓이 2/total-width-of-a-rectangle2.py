n = int(input())
grid = [[0 for _ in range(200)] for _ in range(200)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            grid[i+100][j+100] = 1
area = 0
for row in grid:
    for each in row:
        if each:
            area += 1
print(area)