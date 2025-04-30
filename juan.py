from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://connect.wofford.edu/myWofford/registrar/courseSchedule.aspx"


class Scraper(object):
  def __init__(self):
    self.courses = {}  # dictionary of courses mapped to available seats
    self.watchlist = {}  # dictionary of courses mapped to lists of emails

  def setup_driver(self):
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  

  #Puts it in a dictionary
  def scrape(self):
    driver = Scraper.setup_driver()
    driver.get(URL)

    # Find table rows (excluding headers)
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")[1:]

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        details = [col.text.strip() for col in columns]

        if details and len(details) >= 12:  # Ensures valid row structure
            crn = details[0]  # CRN as the key
            subject = details[1]
            course_number = details[2]
            title = details[10]
            days = details[13]
            time = details[14]
            instructor = details[20]
            available_seats = int(details[19]) if details[19].isdigit() else 0  # Convert to integer

# Here is when it builds the dictionary.
            self.courses[crn] = {
                "subject": subject,
                "course_number": course_number,
                "title": title,
                "days": days,
                "time": time,
                "instructor": instructor,
                "available_seats": available_seats
            }

    driver.quit()
    return self.courses


  def rewatch(self):
    # pull the newest watchlist
    lines = []
    with open('watchlist.txt') as fp:
      lines = fp.readlines()
    self.watchlist = {}
    for line in lines:
      crn, email = line.strip().split()
      if crn not in self.watchlist:
        self.watchlist[crn] = []
      self.watchlist[crn].append(email)
  
  def notify(self):
    lines = []
    with open('courselist.txt') as fp:
      lines = fp.readlines()
    for line in lines:
      crn, available = line.strip().split()
      available = int(available)
      if available > 0:
        for email in self.watchlist[crn]:
          # send an email
          print(f'Sending email to {email}...')
  


def run_monitor():
  scraper = Scraper()
  # this would be a loop of some kind
  for i in range(1):
    scraper.scrape()
    scraper.rewatch()
    scraper.notify()


if __name__ == '__main__':
  run_monitor()

  