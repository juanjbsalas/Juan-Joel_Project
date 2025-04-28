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
    """API to track a course based on form submission."""
    
    # Extract form data (use .form because it's an HTML form submission)
    user_firstname = request.form.get("user_firstname")
    user_lastname = request.form.get("user_lastname")
    user_personal_email = request.form.get("user_personal_email")
    user_wofford_email = request.form.get("user_wofford_email")
    phone_number = request.form.get("phone_number", None)  # Optional
    user_crn = request.form.get("user_crn")

    # Basic validation: Ensure required fields are present
    if not user_personal_email or not user_crn:
        return jsonify({"error": "Personal email and CRN are required"}), 400

    # Save data to database (adjust function accordingly)
    add_request(
        firstname=user_firstname,
        lastname=user_lastname,
        personal_email=user_personal_email,
        wofford_email=user_wofford_email,
        phone=phone_number,
        crn=user_crn
    )

    return jsonify({
        "message": f"Tracking request added for {user_firstname} {user_lastname} ({user_personal_email}) - CRN {user_crn}"
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
