import time
from flask import Flask, request, render_template
import threading
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from tracking import watchlist
from scraper import monitor_course_availability, scrape_courses
from notifier import send_email


app = Flask(__name__)

# We'll keep a list of user watch requests
watchlist = []

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        course_CRN = request.form['course_CRN']
        email = request.form['email']
        watchlist.append({'course_CRN': course_CRN, 'email': email})
        return 'Successfully added!'
    return '''
        <form method="post">
            Course Code: <input type="text" name="course_CRN"><br>
            Email: <input type="text" name="email"><br>
            <input type="submit">
        </form>
    '''

def background_running_scraper():
    while True:
        course_data = scrape_courses
        monitor_course_availability(course_data)
        time.sleep(120) #Checking data every 2 minutes


if __name__ == "__main__":
    threading.Thread(target=background_running_scraper, daemon=True).start()
    app.run(debug=True)
