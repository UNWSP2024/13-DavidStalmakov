# David Stalmakov, 12/3/2025.
# Program 4
import sqlite3

DB_NAME = "phonebook.db"

def show_menu():
    print("\nPHONEBOOK MENU")
    print("1. Add a new entry")
    print("2. Look up a phone number")
    print("3. Change a phone number")
    print("4. Delete an entry")
    print("5. Display all entries")
    print("6. Exit")

def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            try:
                cur.execute(f"INSERT INTO Entries (Name, PhoneNumber) VALUES ('{name}', '{phone}')")
                conn.commit()
                print(f"Added {name} with phone number {phone}.")
            except sqlite3.IntegrityError:
                print("An entry with that name already exists.")

        elif choice == "2":
            name = input("Enter name to look up: ").strip()
            cur.execute(f"SELECT PhoneNumber FROM Entries WHERE Name = '{name}'")
            result = cur.fetchone()
            if result:
                print(f"{name}'s phone number is {result[0]}.")
            else:
                print("No entry found for that name.")

        elif choice == "3":
            name = input("Enter name to change phone number: ").strip()
            cur.execute(f"SELECT PhoneNumber FROM Entries WHERE Name = '{name}'")
            if cur.fetchone():
                new_phone = input("Enter new phone number: ").strip()
                cur.execute(f"UPDATE Entries SET PhoneNumber = '{new_phone}' WHERE Name = '{name}'")
                conn.commit()
                print(f"Updated {name}'s phone number to {new_phone}.")
            else:
                print("No entry found for that name.")

        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            cur.execute(f"SELECT PhoneNumber FROM Entries WHERE Name = '{name}'")
            if cur.fetchone():
                cur.execute(f"DELETE FROM Entries WHERE Name = '{name}'")
                conn.commit()
                print(f"Deleted entry for {name}.")
            else:
                print("No entry found for that name.")

        elif choice == "5":
            cur.execute("SELECT Name, PhoneNumber FROM Entries ORDER BY Name")
            rows = cur.fetchall()
            if rows:
                print("\nAll entries:")
                for row in rows:
                    print(f"{row[0]}: {row[1]}")
            else:
                print("No entries found.")

        elif choice == "6":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please enter 1-6.")

    conn.close()

if __name__ == "__main__":
    main()
