a,b = map(int, input().split())

def calculate(a,b):
    if a>b:
        a,b = b,a
    return a+10, b*2

print(*calculate(a,b))