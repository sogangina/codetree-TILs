command = input()
direction = ([0,1], [-1,0], [0,-1], [1,0]) #북서남동 L
coordinate = [0,0]
d = 0

for c in command:
    if c == 'L':
        d = (d+1)%4
    elif c == 'R':
        d = (d+3)%4
    else:
        coordinate[0] += direction[d][0]
        coordinate[1] += direction[d][1]

print(coordinate[0], coordinate[1])