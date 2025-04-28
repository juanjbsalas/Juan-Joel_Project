from flask import Flask, request, render_template
import threading

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

if __name__ == "__main__":
    app.run(debug=True)
