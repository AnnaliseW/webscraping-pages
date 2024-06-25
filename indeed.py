from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Setup chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the Chrome webdriver service
webdriver_service = Service(ChromeDriverManager().install())

# Start the browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# List to store job details
job_list = []

#search word that can be replaced to scrape 
search = 'Devops'

url = f'https://www.indeed.com/jobs?q={search}&l=&from=searchOnHP'

# Open the webpage
driver.get(url)

wait = WebDriverWait(driver, 10)
jobs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-5lfssm.eu4oa1w0')))

for job in jobs:
    job_info = {}
    try:

        company = job.find_element(By.CLASS_NAME, 'css-63koeb.eu4oa1w0').text
        
        title = job.find_element(By.CLASS_NAME, 'jobTitle.css-198pbd.eu4oa1w0').text
        
        link = job.find_element(By.TAG_NAME, 'a').get_attribute('href')
        
        location = job.find_element(By.CLASS_NAME, 'css-1p0sjhy.eu4oa1w0').text
       

        information = job.find_element(By.CLASS_NAME, 'heading6.tapItem-gutter.metadataContainer.css-z5ecg7.eu4oa1w0').text
        
        job_info['Company'] = company
        job_info['Job Title'] = title
        job_info['Job Link'] = link
        job_info['Location'] = location
        job_info['Information'] = information

        job_list.append(job_info)

        

    except Exception:
        print('not posting')

for job in job_list:
    print(job)
    print()


# Quit the driver
driver.quit()
