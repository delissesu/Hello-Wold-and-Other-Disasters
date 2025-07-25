number = int(input())

is_num = number
reversed_num = 0
while number > 0:
    remainder = number % 10
    reversed_num = (reversed_num * 10) + remainder
    number = number // 10

if is_num == reversed_num:
    print("True")
else:
    print("False")