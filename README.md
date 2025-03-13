# 🎓 Class Availability Notifier

## **📌 Project Overview**
The **Class Availability Notifier** is a web application designed to help students track **course availability** during registration. Instead of **constantly refreshing** the university’s course schedule, students can **enter their email and CRN** (Course Registration Number) and receive **automatic alerts** when a seat becomes available.

## **👨‍💻 Developers**
- **Juan Salas**
- **Joel Gammah**

---

## **🚀 Features**
- 🔹 **Track Course Availability** – Students can register their email & CRN to monitor a class.
- 🔹 **Automated Scraper** – A web scraper periodically checks class seat availability.
- 🔹 **Database Storage** – Student requests are stored in an **SQLite database**.
- 🔹 **Flask API** – Handles tracking requests and serves the frontend.
- 🔹 **Frontend Interface** – Students enter CRNs via a simple **web form**.
- 🔹 **(Coming Soon) Email & SMS Notifications** – Instant alerts when a seat opens up.

---

## **📂 Project Structure**
```bash
Juan-Joel_Project/
│── backend/             # Flask backend (API and routing)
│   ├── app.py           # Main Flask application
│
│── db/                  # Database storage & operations
│   ├── db_setup.py      # Initializes SQLite database
│   ├── db_operations.py # Functions to add/retrieve tracked CRNs
│   ├── students.db      # SQLite database file
│
│── scraper/             # Web scraper to check course availability
│   ├── scraper.py       # Scrapes university course data
│
│── frontend/            # User interface (HTML, CSS, JS)
│   ├── templates/
│   │   ├── index.html   # Webpage (form for students)
│   ├── static/
│   │   ├── script.js    # Handles form submission & API requests
│   │   ├── styles.css   # (Optional) Styles for the webpage
│
│── README.md            # Project documentation
│── requirements.txt     # Dependencies (Flask, Selenium, SQLite)

```
---

## **Run the Flask Backend**
```bash
export PYTHONPATH=$PYTHONPATH:/Users/joelgammah/Desktop/Juan-Joel_Project/
python3 backend/app.py

```

---

## **📡 API Endpoints**
```bash
Method	Endpoint	Description
GET	/	Serves index.html (homepage)
POST	/track	Tracks a course { "email": "example", "crn": "1234" }
GET	/tracked	Retrieves all tracked CRNs
```
---

## **📈 How It Works**

1️⃣ Student visits the web form and enters email & CRN.
2️⃣ Flask stores the request in an SQLite database.
3️⃣ The web scraper continuously checks for seat availability.
4️⃣ When a seat becomes available, the system will (soon) send an email or SMS.


