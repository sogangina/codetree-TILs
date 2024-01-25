a,b,c,d = map(int, input().split())

hour = c - a
print(60 * hour + d - b)