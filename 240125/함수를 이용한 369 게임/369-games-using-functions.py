def is3(n):
    return False if n%3 else True

def is369(n):
    result = False
    n = str(n)
    for i in n:
        if i in '369':
            result = True
            break
    return result

a,b = map(int, input().split())

print(len([i for i in range(a,b+1) if is3(i) or is369(i)]))