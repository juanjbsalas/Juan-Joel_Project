from flask import Flask, request, jsonify, render_template
from db.db_operations import add_request, get_tracked_crns
import os

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")


@app.route("/")
def index():
    """Serve the index.html page."""
    return render_template("index.html")

@app.route("/track", methods=["POST"])
def track_class():
    """API to track a course based on email & CRN."""
    data = request.json
    email = data.get("email")
    crn = data.get("crn")
    phone = data.get("phone", None)

    if not email or not crn:
        return jsonify({"error": "Email and CRN are required"}), 400

    add_request(email, crn, phone)  # Save to SQLite database
    return jsonify({"message": f"Tracking request added for {email} - CRN {crn}"}), 201

if __name__ == "__main__":
    app.run(debug=True)
