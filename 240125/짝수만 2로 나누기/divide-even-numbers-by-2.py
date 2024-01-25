def function(n, array):
    for i in range(n):
        if array[i] % 2 == 0:
            array[i] *= 0.5
            array[i] = int(array[i])

n = int(input())
array = list(map(int, input().split()))

function(n, array)

print(*array)