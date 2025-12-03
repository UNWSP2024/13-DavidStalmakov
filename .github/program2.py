# David Stalmakov, 12/3/2025
# Cities Database
# This program displays the information from the created cities file
import sqlite3

def show_menu():
    print("\nCITY DATABASE MENU")
    print("1. List cities by population (ascending)")
    print("2. List cities by population (descending)")
    print("3. List cities by name")
    print("4. Display total population")
    print("5. Display average population")
    print("6. Display city with highest population")
    print("7. Display city with lowest population")
    print("8. Exit")

def main():
    conn = sqlite3.connect("cities.db")
    cur = conn.cursor()


    show_menu()
    choice = input("Enter your choice (1–7): ")

    if choice == "1":
        cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC")
        for row in cur.fetchall():
            print(row)

    elif choice == "2":
        cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC")
        for row in cur.fetchall():
            print(row)

    elif choice == "3":
        cur.execute("SELECT CityName, Population FROM Cities ORDER BY CityName ASC")
        for row in cur.fetchall():
            print(row)

    elif choice == "4":
        cur.execute("SELECT SUM(Population) FROM Cities")
        total = cur.fetchone()[0]
        print(f"Total population of all cities: {total:,}")

    elif choice == "5":
        cur.execute("SELECT AVG(Population) FROM Cities")
        avg = cur.fetchone()[0]
        print(f"Average population: {avg:,.2f}")

    elif choice == "6":
        cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1")
        city = cur.fetchone()
        print(f"City with highest population: {city[0]} ({city[1]:,})")

    elif choice == "7":
        cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1")
        city = cur.fetchone()
        print(f"City with lowest population: {city[0]} ({city[1]:,})")

    else:
        print("Invalid choice. Try again.")

    conn.close()

if __name__ == "__main__":
    main()