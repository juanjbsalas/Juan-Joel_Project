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


## **📈 How It Works**

1️⃣ Student visits the web form and enters email & CRN.
2️⃣ Flask stores the request in an SQLite database.
3️⃣ The web scraper continuously checks for seat availability.
4️⃣ When a seat becomes available, the system will (soon) send an email or SMS.

## **📜 License**

This project is open-source under the MIT License.
