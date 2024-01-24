n = int(input())
array = list(map(int, input().split()))
array.sort()
plus = array[-1] * array[-2] * array[-3]
minus = array[0] * array[1] * array[-1]
print(max(plus, minus))