d = 'WSNE'
dx,dy = [-1,0,0,1],[0,-1,1,0]
direction = {i:[j,k] for i,j,k in zip(d,dx,dy)}
coordinate = [0,0]

n = int(input())
for _ in range(n):
    a,b = input().split()
    b = int(b)
    coordinate[0] += direction[a][0] * b
    coordinate[1] += direction[a][1] * b

print(coordinate[0], coordinate[1])