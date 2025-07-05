from typing import Tuple

def getUserInput() -> Tuple[float, float]:
    try:
        number_one: float = float(input("Enter the first number: "))
        number_two: float = float(input("Enter the second number: "))
        return number_one, number_two
    except ValueError:
        print("Invalid input. Please enter numeric values for both numbers.")
        exit(1)

def performCalculations(num1: float, num2: float) -> Tuple[float, float, float, float | str]:
    addition: float = num1 + num2
    subtraction: float = num1 - num2
    multiplication: float = num1 * num2
    
    division: float | str = "Error: Cannot divide by zero." if num2 == 0 else num1 / num2
    
    return addition, subtraction, multiplication, division

def displayResults(num1: float, num2: float, add: float, sub: float, mult: float, div: float | str) -> None:
    print("\n--- Simple Calculator Results ---")
    print(f"Addition: {num1} + {num2} = {add}")
    print(f"Subtraction: {num1} - {num2} = {sub}")
    print(f"Multiplication: {num1} * {num2} = {mult}")
    
    if isinstance(div, str):
        print(f"Division: {num1} / {num2} = {div}")
    else:
        print(f"Division: {num1} / {num2} = {div:.2f}")

def main() -> None:
    number_one, number_two = getUserInput()
    addition, subtraction, multiplication, division = performCalculations(number_one, number_two)
    displayResults(number_one, number_two, addition, subtraction, multiplication, division)

if __name__ == "__main__":
    main()