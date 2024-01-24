n,t = map(int, input().split())
array = list(map(int, input().split()))
i = 0
j = 0
for element in array:
    if element > t :
        i += 1
    else:
        if i > j:
            j = i
            i = 0
print(j)