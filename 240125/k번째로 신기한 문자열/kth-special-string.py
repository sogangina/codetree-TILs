n,k,T = input().split()
n = int(n)
k = int(k)
array = [input() for _ in range(n)]

def startswith(T, str_):
    result = True
    for i,j in zip(T, str_):
        if i != j:
            result = False
    return result

candidate = sorted([each for each in array if startswith(T, each)])

print(candidate[k-1])