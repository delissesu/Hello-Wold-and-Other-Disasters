import random
from typing import Tuple, Union

Number = Union[int, float]

# Step 1: Define the math question function
def mathQueston() -> Tuple[str, Number]:
    num1: int = random.randint(1, 10)
    num2: int = random.randint(1, 10)
    
    operator_list: list[str] = ["+", "-", "*", "/"]
    operator: str = random.choice(operator_list)

    question: str = f"{num1} {operator} {num2}"
    answer: Number

    match operator:
        case "+":
            answer = num1 + num2
        case "-":
            answer = num1 - num2
        case "*":
            answer = num1 * num2
        case "/":
            # Ensure num2 is not zero for division
            if num2 == 0: 
                return mathQueston()
            # For simpler quiz, let's make division result in an integer if possible
            if num1 % num2 == 0:
                answer = num1 // num2
            else:
                # If not perfectly divisible, re-generate or accept float
                answer = round(num1 / num2, 2) 
        case _: 
            raise ValueError("Invalid operator selected")

    return question, answer

# Step 2: Main quiz function
def mathQuiz() -> None:
    score: int = 0
    total_questions: int = 3

    print("\n--- Welcome to Math Quiz Game ---")
    print("You will be presented with math problems, and you need to find the correct answer.")

    for round_num in range(total_questions):
        question_text, correct_answer = mathQueston()

        print(f"\nQuestion {round_num + 1}: What is {question_text}?")

        while True:
            try:
                user_input_str: str = input("Enter your answer: ")
                user_answer: Number
                if '.' in user_input_str:
                    user_answer = float(user_input_str)
                else:
                    user_answer = int(user_input_str)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if isinstance(correct_answer, float):
            if abs(user_answer - correct_answer) < 0.01 :
                print("Correct answer!")
                score += 1
            else:
                print(f"Wrong answer! The correct answer is {correct_answer}")
        else: 
            if user_answer == correct_answer:
                print("Correct answer!")
                score += 1
            else:
                print(f"Wrong answer! The correct answer is {correct_answer}")

    print("\n--- Game Over ---")
    print(f"Your final score: {score}/{total_questions}")

    if score == total_questions:
        print("Congratulations! You answered all the questions correctly.")
    elif score >= total_questions / 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing! You can do better next time.")

# Step 3: Run the game
if __name__ == "__main__":
    mathQuiz()