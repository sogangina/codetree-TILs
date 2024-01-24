n,s = map(int, input().split())
array = list(map(int, input().split()))

whole = sum(array)
difference = whole

for i in range(n):
    for j in range(i,n):
        exclude = array[i] + array[j]
        difference = min(difference, abs(s + exclude - whole))

print(difference)