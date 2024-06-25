from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the Chrome webdriver service
webdriver_service = Service(ChromeDriverManager().install())

# Start the browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

state = 'Illinois'
search = 'Devops'

url = f'https://apply.clickjobs.io/jobs/search?q={search}&l={state}%2C+USA&lat=40&long=-89.25&d='
# Open the webpage
driver.get(url)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.jobList')))

jobs_list = []

jobs = driver.find_elements(By.CLASS_NAME, 'job-listing.logo')

for job in jobs:
    job_info = {}
    elements = job.find_element(By.CLASS_NAME, 'jobList-introWrap')
    title = elements.find_element(By.CLASS_NAME, 'jobList-title').text
    link = elements.find_element(By.CLASS_NAME, 'jobList-title').get_attribute('href')
    

    companyLocation = job.find_element(By.CLASS_NAME, 'jobList-introMeta').text
    split = companyLocation.split('\n')
    company = split[0]
    location = split[1]
   

    date = job.find_element(By.CLASS_NAME, 'jobList-date.text-muted.u-textNoWrap').text
    

    
    job_info['Company'] = company
    job_info['Job Title'] = title
    job_info['Job Link'] = link
    job_info['Location'] = location
    job_info['Date Posted'] = date
    
    jobs_list.append(job_info)


for job in jobs_list:
    print(job)
    print()


test = []
yourWelcome = {}




print(test)



driver.quit()
