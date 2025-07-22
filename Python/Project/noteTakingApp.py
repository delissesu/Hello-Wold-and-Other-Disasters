import pathlib
import time

NOTES_FILE = pathlib.Path(__file__).parent / "notes.txt"


def display_menu() -> None:
    print("\n=== Note Taking App Menu ===")
    print("1. Add New Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Delete All Notes")
    print("5. Exit")
    print("==========================")


def add_note() -> None:
    note_text = input("Enter your note: ").strip()
    if not note_text:
        print("Note cannot be empty.")
        return

    try:
        with NOTES_FILE.open("a", encoding="utf-8") as f:
            f.write(note_text + "\n")
        print("Note added successfully!")
    except OSError as e:
        print(f"Error: Could not write to file {NOTES_FILE}. Reason: {e}")


def view_notes() -> None:
    try:
        with NOTES_FILE.open("r", encoding="utf-8") as f:
            notes = f.readlines()
            if not notes:
                print("\n--- No Notes Found ---")
                return

            print("\n--- All Notes ---")
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")
            print("-------------------")

    except FileNotFoundError:
        print("\n--- No Notes Found ---")
    except OSError as e:
        print(f"Error: Could not read file {NOTES_FILE}. Reason: {e}")


def search_notes() -> None:
    query = input("Enter text to search for: ").strip()
    if not query:
        print("Search term cannot be empty.")
        return

    try:
        with NOTES_FILE.open("r", encoding="utf-8") as f:
            notes = f.readlines()

        # Find all notes containing the query (case-insensitive)
        found_notes = [
            (i, note.strip())
            for i, note in enumerate(notes, 1)
            if query.lower() in note.lower()
        ]

        if not found_notes:
            print(f"\n--- No notes found containing '{query}' ---")
            return

        print(f"\n--- Found {len(found_notes)} note(s) containing '{query}' ---")
        for i, note in found_notes:
            print(f"{i}. {note}")
        print("-----------------------------------------")
    except FileNotFoundError:
        print("\n--- No Notes Found ---")
    except OSError as e:
        print(f"Error: Could not read file {NOTES_FILE}. Reason: {e}")


def delete_notes() -> None:
    confirmation = (
        input("Are you sure you want to delete all notes? (y/n): ").strip().lower()
    )
    if confirmation != "y":
        print("Deletion cancelled.")
        return

    try:
        with NOTES_FILE.open("w", encoding="utf-8"):
            pass  # Opening in 'w' mode and closing is enough to clear it
        print("All notes deleted successfully!")
    except FileNotFoundError:
        print("\n--- No Notes Found to Delete ---")
    except OSError as e:
        print(f"Error: Could not write to file {NOTES_FILE}. Reason: {e}")


def main() -> None:
    actions = {
        "1": add_note,
        "2": view_notes,
        "3": search_notes,
        "4": delete_notes,
    }

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Exiting the program. Goodbye!")
            time.sleep(1)
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
