from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Constants
URL = "https://connect.wofford.edu/myWofford/registrar/courseSchedule.aspx"
WAIT_TIME = 300  # Scraper runs every 5 minutes

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

        if details and len(details) >= 12:  # Ensure valid row structure
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

# Function to validate CRN input
def get_valid_crn(course_dict):
    while True:
        desired_crn = input("Enter the CRN for the course you would like to be notified about: ").strip()

        if desired_crn in course_dict:
            confirmation = input(f"Is the course '{course_dict[desired_crn]['title']}' correct? (Y/N): ").strip().upper()
            if confirmation == 'Y':
                print("Great! We will notify you whenever this course has seats available!")
                return desired_crn
            elif confirmation == 'N':
                print("Please enter the correct CRN.")
            else:
                print("Invalid response. Type 'Y' for Yes or 'N' for No.")
        else:
            print("Invalid CRN. Please enter a valid one.")

# Function to monitor course availability
def monitor_course_availability(course_dict, desired_crn):
    print(f"Monitoring availability for CRN {desired_crn}...")

    while True:
        course_dict = scrape_courses()  # Refresh course data

        if desired_crn in course_dict:
            available_seats = course_dict[desired_crn]["available_seats"]
            if available_seats > 0:
                print(f"🚀 ALERT: Course '{course_dict[desired_crn]['title']}' (CRN: {desired_crn}) has {available_seats} seat(s) available! Register now!")
                break
            else:
                print(f"No seats available for {course_dict[desired_crn]['title']} (CRN: {desired_crn}). Checking again in {WAIT_TIME // 60} minutes...")
        else:
            print("Course not found. Retrying...")

        time.sleep(WAIT_TIME)  # Wait before checking again

# Main Execution
if __name__ == "__main__":
    print("Fetching course data...")
    course_data = scrape_courses()
    crn_to_track = get_valid_crn(course_data)
    monitor_course_availability(course_data, crn_to_track)
