base = int(input())
exp = int(input())

result = 1

while exp > 0:
    result *= base
    exp -= 1

print(result)