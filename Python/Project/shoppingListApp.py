from typing import List

def AddItem(shopping_items: List[str], item_name: str) -> None:
    shopping_items.append(item_name)
    print(f"'{item_name}' has been added to your shopping list.")

def RemoveItem(shopping_items: List[str], item_name: str) -> None:
    if not shopping_items:
        print("Your shopping list is already empty.")
        return
    try:
        shopping_items.remove(item_name)
        print(f"'{item_name}' has been removed from your shopping list.")
    except ValueError:
        print(f"'{item_name}' is not in your shopping list.")

def ViewList(shopping_items: List[str]) -> None:
    if not shopping_items:
        print("Your shopping list is empty.")
    else:
        print("\n--- Your Shopping List ---")
        for index, item in enumerate(shopping_items, start=1):
            print(f"{index}. {item}")

def ClearList(shopping_items: List[str]) -> None:
    shopping_items.clear()
    print("Your shopping list has been cleared.")

def IsListEmpty(shopping_items: List[str]) -> bool:
    return not shopping_items

def DisplayMainMenu() -> None:
    print("\n--- Shopping List Menu ---")
    print("1. View Shopping List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Clear Shopping List")
    print("5. Quit")

def Main() -> None:
    current_shopping_list: List[str] = []  # The shopping list is now a local variable

    while True:
        DisplayMainMenu()
        choice: str = input("Enter your choice: ")

        if choice == "1":
            ViewList(current_shopping_list)
        elif choice == "2":
            item_to_add: str = input("Enter the item you want to add: ")
            if item_to_add: 
                AddItem(current_shopping_list, item_to_add)
            else:
                print("Item name cannot be empty.")
        elif choice == "3":
            if IsListEmpty(current_shopping_list):
                print("Your shopping list is empty. Nothing to remove.")
            else:
                ViewList(current_shopping_list)  
                item_to_remove: str = input("Enter the item name you want to remove: ")
                if item_to_remove: 
                    RemoveItem(current_shopping_list, item_to_remove)
                else:
                    print("Item name cannot be empty.")
        elif choice == "4":
            ClearList(current_shopping_list)
        elif choice == "5":
            print("Thank you for using the Shopping List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Main()