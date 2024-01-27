n = input()

decoded = 0
for i in range(len(n)):
    decoded = decoded*2 + int(n[i])

decoded *= 17

binary = []
while True:
    if decoded < 2:
        binary.append(decoded)
        break
    binary.append(decoded%2)
    decoded //= 2

for i in binary[::-1]:
    print(i, end='')