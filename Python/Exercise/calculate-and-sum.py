number_one = int(input())
number_two = int(input())

# product = number_one * number_two
# if product <= 1000:
#     print(product)
# else:
#     print(number_one + number_two)
    
def calculateSum(numOne, numTwo):
    product = numOne * numTwo
    if product <= 1000:
        return product
    else:
        return numOne + numTwo
    
calculate_and_sum = calculateSum(number_one, number_two)
print(calculate_and_sum)