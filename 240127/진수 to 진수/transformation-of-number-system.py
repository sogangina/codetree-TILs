a,b = map(int, input().split())
n = input()

decimal = 0
for i in range(len(n)):
    decimal = decimal*a + int(n[i])

binary = []
while True:
    if decimal < b:
        binary.append(decimal)
        break
    binary.append(decimal%b)
    decimal //= b

for i in binary[::-1]:
    print(i, end='')