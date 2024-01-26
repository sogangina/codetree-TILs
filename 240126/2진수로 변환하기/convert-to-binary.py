def decode(n):
    decimal = []
    while n > 2:
        decimal.append(n%2)
        n //= 2
    decimal.append(n%2)
    return decimal[::-1]
    
n = int(input())
for i in decode(n):
    print(i, end='')