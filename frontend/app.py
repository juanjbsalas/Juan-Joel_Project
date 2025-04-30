import time
from flask import Flask, request, jsonify, render_template, redirect, url_for
import threading
import os


#from backend.tracking import watchlist
#from backend.scraper import monitor_course_availability, scrape_courses
#from backend.notifier import send_email

desktop_path = os.path.expanduser("~/Desktop/Juan-Joel_Project") # Later this should save to an online data base
os.makedirs(desktop_path, exist_ok=True)  #Ensures folder exists

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        course_CRN = request.form['course_CRN']
        email = request.form['email']
        
        filename = os.path.join(desktop_path, 'desired_classes.txt')
        with open(filename, 'w') as fp:
            fp.write(f"{course_CRN} {email}\n")

        #Process file
 #       result = process_input(filename) #! I think this line is not relaly needed
        
        return 'Successfully added!'
    return '''
        <form method="post">
            Course Code: <input type="text" name="course_CRN"><br>
            Email: <input type="text" name="email"><br>
            <input type="submit">
        </form>
    '''

"""
def background_running_scraper():
    while True:
        course_data = scrape_courses()  #This returns the course dictionary
        monitor_course_availability(course_data)
        time.sleep(120) #Checking data every 2 minutes"""



if __name__ == "__main__" or __name__ == "frontend.app":
    app.run(debug=True)

