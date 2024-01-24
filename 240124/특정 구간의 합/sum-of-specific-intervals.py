# 누적합 prefix sum

n,m = map(int, input().split())
array = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(m)]

prefix_sum = [0]
for element in array:
    prefix_sum.append(prefix_sum[-1] + element)

for i,j in query:
    print(prefix_sum[j] - prefix_sum[i-1])