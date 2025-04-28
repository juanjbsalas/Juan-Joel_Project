from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from backend.notifier import send_email
from tracking import watchlist


# Constants
URL = "https://connect.wofford.edu/myWofford/registrar/courseSchedule.aspx"
WAIT_TIME = 60  # Scraper runs every 1 minutes

# Function to set up Selenium WebDriver
def setup_driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to scrape course data
def scrape_courses():
    driver = setup_driver()
    driver.get(URL)

    # Find table rows (excluding headers)
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")[1:]

    # Dictionary to store course data
    course_dict = {}

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        details = [col.text.strip() for col in columns]

        if details and len(details) >= 12:  # Ensuring valid row structure
            crn = details[0]  # CRN as the key
            subject = details[1]
            course_number = details[2]
            title = details[10]
            days = details[13]
            time = details[14]
            instructor = details[20]
            available_seats = int(details[19]) if details[19].isdigit() else 0  # Convert to integer

            course_dict[crn] = {
                "subject": subject,
                "course_number": course_number,
                "title": title,
                "days": days,
                "time": time,
                "instructor": instructor,
                "available_seats": available_seats
            }

    driver.quit()
    return course_dict

# Function to monitor course availability
def monitor_course_availability(course_dict):
    print("Checking for available seats...")

    for request in watchlist:
        crn = request['course_CRN']
        email = request['email']

        if crn in course_dict:
            available_seats = course_dict[crn]["available_seats"]
            if available_seats > 0:
                print(f"🚀 ALERT: {email}, CRN {crn} now has {available_seats} seat(s) available!")
                send_email(email, "Seats Available!", f"Quick! {crn} now has {available_seats} seats available!")
            else:
                print(f"No seats available for {course_dict[crn]['title']} (CRN: {crn}). Checking again soon...")


# Main Execution
if __name__ == "__main__":
    while True:
        print("Fetching course data...")
        course_data = scrape_courses()
        monitor_course_availability(course_data)