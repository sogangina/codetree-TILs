OFFSET = 100
MAX_R = 200

n = int(input())
rects = [tuple(map(int, input().split())) for _ in range(n)]
grid = [[0 for _ in range(MAX_R+1)] for _ in range(MAX_R+1)]

for x1, y1, x2, y2 in rects:
    x1, y1 = x1+OFFSET, y1+OFFSET
    x2, y2 = x2+OFFSET, y2+OFFSET

    for y in range(y1,y2):
        for x in range(x1,x2):
            grid[y][x] = 1

area = 0
for y in range(MAX_R+1):
    for x in range(MAX_R+1):
        if grid[y][x]: area += 1

print(area)