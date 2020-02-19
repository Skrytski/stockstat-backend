from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
URL = 'https://submit.shutterstock.com'
driver = webdriver.Chrome()
driver.get(URL)

# Test
try:
    WebDriverWait(driver, 999).until(EC.url_matches('https://submit.shutterstock.com/dashboard'))
    time.sleep(3)
    driver.get('https://submit.shutterstock.com/earnings?language=en')
    print('Goood')
finally:
    time.sleep(60)
    driver.quit()


# After login try to use Beautiful soup for faster scraping.
