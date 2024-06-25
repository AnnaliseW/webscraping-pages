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

    # Open the webpage
driver.get('https://www.google.com/search?q=devops+jobs+illinois+linkedin&ibp=htl;jobs&sa=X&ved=2ahUKEwiGvOyFz7WGAxUehIkEHQZvBw8QutcGKAF6BAgTEAQ&sxsrf=ADLYWIKTduaFdTReKYPlnRjRboxz-QKYuA:1717080424133#htivrt=jobs&htidocid=XVL-eHaBc7cDhaAAAAAAAA%3D%3D&fpstate=tldetail')

wait = WebDriverWait(driver, 10)

jobs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'iFjolb.gws-plugins-horizon-jobs__li-ed')))


for job in jobs:
    job_info = {}

    company = job.find_element(By.CLASS_NAME, 'vNEEBe').text
    print(company)

    title = job.find_element(By.CLASS_NAME, 'BjJfJf.PUpOsf').text
    print(title)

    location = job.find_element(By.CLASS_NAME, 'Qk80Jf').text
    print(location)

    link = job.find_element(By.XPATH, './/a').get_attribute('href')
    print(link)

    info = job.find_elements(By.CSS_SELECTOR, 'span.LL4CDc')
    excessInfo = ''
    for i in info:
        if i.text != '':
            excessInfo = excessInfo + '\n' + i.text 
    
    excessInfo = excessInfo.replace('\n', '', 1)
    print(excessInfo)

    job_info['Company'] = company
    job_info['Job Title'] = title
    job_info['Job Link'] = link
    job_info['Location'] = location
    job_info['Info'] = excessInfo
    
    job_list.append(job_info)

for job in job_list:
    print(job)
    print()





driver.quit()
