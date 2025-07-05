import time

def getCountdownInput() -> int:
    return int(input("Enter a start value: "))

def Countdown(start_value: int) -> None:
    print("\n--- Countdown Begin ---")
    
    current_value: int = start_value
    
    while current_value > 0:
        print(current_value)
        time.sleep(1)
        current_value -= 1
    
    print("--- Countdown Stop ---")

def main() -> None:
    start_value: int = getCountdownInput()
    Countdown(start_value)

if __name__ == "__main__":
    main()