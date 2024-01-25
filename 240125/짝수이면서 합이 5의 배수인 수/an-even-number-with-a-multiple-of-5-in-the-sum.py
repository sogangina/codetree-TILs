def function(n):
    quotient = n // 10
    remainder = n % 10
    even = remainder in [0,2,4,6,8]
    five = (quotient + remainder) % 5 == 0
    if even and five:
        return "Yes"
    else:
        return "No"

n = int(input())
print(function(n))