import sqlite3

def add_request(email, crn, phone=None):
    """Stores a student's CRN tracking request in the database."""
    conn = sqlite3.connect("db/students.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO requests (email, crn, phone) VALUES (?, ?, ?)", (email, crn, phone))

    conn.commit()
    conn.close()
    print(f"Tracking request added: {email} -> CRN {crn}")

def get_tracked_crns():
    """Retrieves all tracked CRNs and associated emails."""
    conn = sqlite3.connect("db/students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT email, crn, phone FROM requests")
    tracked_requests = cursor.fetchall()

    conn.close()
    return tracked_requests

# Example usage (for testing)
if __name__ == "__main__":
    print("Fetching tracked CRNs...")
    tracked_crns = get_tracked_crns()
    for email, crn, phone in tracked_crns:
        print(f"Tracking: {email} wants CRN {crn} (Phone: {phone})")
