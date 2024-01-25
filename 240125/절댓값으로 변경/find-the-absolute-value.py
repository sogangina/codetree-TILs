def function(n, array):
    for i in range(n):
        array[i] = abs(array[i])

n = int(input())
array = list(map(int, input().split()))
function(n, array)
print(*array)