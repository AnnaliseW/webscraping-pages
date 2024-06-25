from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
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

url = f'https://www.dice.com/jobs?q={search}&location=Illinois,%20USA&latitude=40.6331249&longitude=-89.3985283&countryCode=US&locationPrecision=State&adminDistrictCode=IL&radius=30&radiusUnit=mi&page=1&pageSize=20&language=en&eid=0345'

# Open the webpage
driver.get(url)


def scroll_to_element(element):
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()


wait = WebDriverWait(driver, 10)
jobs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card.search-card')))


for job in jobs:
    job_info = {}
    try:
        scroll_to_element(job)
        company = job.find_element(By.CLASS_NAME, 'ng-star-inserted').text
        
        

        title = job.find_element(By.TAG_NAME, 'a')

        title = title.text
        
    
    
        location = job.find_element(By.CLASS_NAME, 'search-result-location').text
        

        date = job.find_element(By.CSS_SELECTOR, 'span.posted-date').text
        
        jobType = job.find_element(By.CLASS_NAME, 'card-position-type').text
       
        


        title_element = job.find_element(By.CLASS_NAME, 'card-title-link')
        

        # Click on the title to open the job details in a new tab
        title_element.click()


        # Wait for the new tab to open and switch to it
        wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])

        # Wait for the job detail page to load and get the URL
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        job_link = driver.current_url
        

        # Close the new tab and switch back to the original tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        
      

        job_info['Company'] = company
        job_info['Job Title'] = title
        job_info['Job Link'] = job_link
        job_info['Location'] = location
        job_info['Date Posted'] = date
        job_info['Job Type'] = jobType

        job_list.append(job_info)


    
    except Exception:
        print('not posting')

for job in job_list:
    print(job)
    print()

# Quit the driver
driver.quit()
