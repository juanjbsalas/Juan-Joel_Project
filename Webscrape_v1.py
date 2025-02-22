from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the course schedule webpage
url = "https://connect.wofford.edu/myWofford/registrar/courseSchedule.aspx"
driver.get(url)

# Find the table rows (skip headers)
rows = driver.find_elements(By.CSS_SELECTOR, "table tr")[1:]  # Adjust selector as needed

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
        
        # Convert "Available" seats to an integer
        available_seats = details[19] #if details[11].isdigit() else 0  

        # Store in dictionary
        course_dict[crn] = [
            [subject, course_number, title, days, time, instructor], 
            available_seats
        ]

print("---------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------")
print(details)


# Close the browser
driver.quit()

# Print or return the dictionary
print(course_dict)
