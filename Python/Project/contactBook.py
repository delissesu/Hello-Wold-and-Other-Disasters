from typing import Dict
import time

ContactBook = Dict[str, Dict[str, str]]
contact_book: ContactBook = {}

def DisplayMenu() -> None:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

def AddContact() -> None:
    print("\n--- Adding New Contact ---")
    
    contact_name: str = input("Enter contact name: ").strip()
    contact_phone: str = input("Enter contact number: ").strip()
    contact_email: str = input("Enter contact email: ").strip()
    
    # Store contact information in the contact book
    contact_book[contact_name] = {
        "phone": contact_phone,
        "email": contact_email
    }
    
    print(f"\n{contact_name} has been added to your contact book!")

def ViewContacts() -> None:
    if not contact_book:
        print("\nYour contact book is empty.")
        return
    
    print("\n--- All Contacts ---")
    for contact_name, contact_info in contact_book.items():
        print(f"\nName: {contact_name}")
        print(f"Phone: {contact_info['phone']}")
        print(f"Email: {contact_info['email']}")
        print("-" * 30)

def SearchContact() -> None:
    # Search spedific information by contact name
    search_name: str = input("\nEnter contact name to search: ").strip()
    
    if search_name in contact_book:
        contact_info = contact_book[search_name]
        print(f"\n--- Contact Details for {search_name} ---")
        print(f"Name: {search_name}")
        print(f"Phone: {contact_info['phone']}")
        print(f"Email: {contact_info['email']}")
    else:
        print(f"\n{search_name} not found in your contact book.")

def EditContact() -> None:
    edit_name: str = input("\nEnter contact name to edit: ").strip()
    
    if edit_name not in contact_book:
        print(f"\n{edit_name} not found in your contact book.")
        return
    
    print(f"\n--- Editing Contact: {edit_name} ---")
    print("Current information:")
    print(f"Phone: {contact_book[edit_name]['phone']}")
    print(f"Email: {contact_book[edit_name]['email']}")
    
    # Get new information
    new_phone: str = input("\nEnter new phone number: ").strip()
    new_email: str = input("Enter new email: ").strip()
    
    # Update the contact
    contact_book[edit_name] = {
        "phone": new_phone,
        "email": new_email
    }
    
    print(f"\n{edit_name}'s information has been updated!")

def DeleteContact() -> None:
    delete_name: str = input("\nEnter contact name to delete: ").strip()
    
    if delete_name in contact_book:
        del contact_book[delete_name]
        print(f"\n{delete_name} has been deleted from your contact book.")
    else:
        print(f"\n{delete_name} not found in your contact book.")

def GetUserChoice() -> str:
    return input("\nEnter your choice (1-6): ").strip()

def Main() -> None:
    print("Welcome to Your Contact Book!")
    
    while True:
        DisplayMenu()
        choice: str = GetUserChoice()
        
        if choice == "1":
            AddContact()
        elif choice == "2":
            ViewContacts()
        elif choice == "3":
            SearchContact()
        elif choice == "4":
            EditContact()
        elif choice == "5":
            DeleteContact()
        elif choice == "6":
            print("\nExiting the program. Goodbye!")
            time.sleep(1)
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    Main()