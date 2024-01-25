def function(n, array):
    array.sort()
    new = [array[i]+array[2*n-1-i] for i in range(0,n)]
    return max(new)

n = int(input())
array = list(map(int, input().split()))
print(function(n, array))