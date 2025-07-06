# Step 1: Get user inputs for two numbers
def GetNumber(numInput: str) -> float:
    return float(input(numInput))

number_one: float = GetNumber("Enter first number: ")
number_two: float = GetNumber("Enter second number: ")

# Step 2: Compare the numbers
def CompareNumbers(a: float, b: float) -> None:
    print("\n--- Number Comparison Results ---")
    
    if a == b:
        print("Both numbers are equal")
    elif a > b:
        print(f"{a} is greater than {b}.")
    else:
        print(f"{b} is greater than {a}.")

CompareNumbers(number_one, number_two)
    
# Step 3: Check if any number is zero
def CheckZeroInput(a: float, b: float) -> None:
    if a == 0 or b == 0:
        print("At least one number is zero.")
    else:
        print("Both numbers are non-zero.")

CheckZeroInput(number_one, number_two)