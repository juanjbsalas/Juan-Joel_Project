import sqlite3

# Connect to SQLite (creates 'students.db' if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create the 'requests' table (if not exists)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        crn TEXT NOT NULL,
        phone TEXT
    )
""")

# Save and close the connection
conn.commit()
conn.close()

print("Database initialized successfully!")
