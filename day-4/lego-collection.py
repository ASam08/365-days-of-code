import sqlite3

def main():
    with sqlite3.connect('lego_collection.db') as conn:
        cursor = conn.cursor()

        try:
            get_sets(cursor)
        except sqlite3.OperationalError as e:
            build_sets_table(cursor)

        while True:
            choice = chooser()
            if choice == '1':
                get_sets(cursor)
            elif choice == '2':
                add_set(conn, cursor)
            elif choice == '3':
                print("\nGoodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2 or 3.")

def chooser():
    print("\nWhat would you like to do?\n")
    print("1. Veiw all sets")
    print("2. Add a new set")
    print("3. Quit\n")
    choice = input("Enter the number of your choice: ")
    return choice

def add_set(conn, cursor):
    set_name = input("\nEnter the name of the set: ")
    set_id = input("Enter the set ID: ")

    cursor.execute("INSERT INTO Sets (Name, Set_ID) VALUES (?, ?)", (set_name, set_id))
    conn.commit

    print(f'\nSet "{set_name}" with ID {set_id} added to the database.\n')
    input("Press Enter to continue...")


def build_sets_table(cursor):
    cursor.execute("CREATE TABLE Sets (ID TEXT PRIMARY KEY, Name TEXT, Set_ID INT)")
    print("Sets table created.")


def get_sets(cursor):
    cursor.execute("SELECT Set_ID, Name FROM Sets")
    sets = cursor.fetchall()
    if sets:
        print("Your LEGO Sets:")
        for set_id, name in sets:
            print(f"Set ID: {set_id}, Name: {name}")
        print()
        input("Press Enter to continue...")
    else:
        print("No sets found in the database.\n")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()