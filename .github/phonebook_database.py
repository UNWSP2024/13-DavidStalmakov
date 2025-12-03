import sqlite3

DB_NAME = "phonebook.db"

def create_db_and_table():
    """Create the database and Entries table if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Entries (Name TEXT PRIMARY KEY,
            PhoneNumber TEXT)""")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db_and_table()