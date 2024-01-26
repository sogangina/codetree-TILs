n = [int(i) for i in input()]

binary = 0
for i in range(len(n)):
    binary = binary*2 + n[i]

print(binary)