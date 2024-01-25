def function(n, array):
    array.sort()
    return array[n] + array[n-1]

n = int(input())
array = list(map(int, input().split()))
print(function(n, array))