num = int(input())
# while num > 0:
#     digit = num % 10
#     num = num // 10
#     print(digit, end=" ")

digit_list = []
while num > 0:
    digit = num % 10
    number = num // 10
    digit_list.append(digit)
    num = number

digit_list = digit_list[::-1]
print(digit_list)

for _ in digit_list:
    print(_, end=" ")