from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service('driver/chromedriver')
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get('https://www.youtube.com/watch?v=BQ-9e13kJ58')
try:
    element = WebDriverWait(browser, 10000).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="logo"]'))
    ).click()
except:
    print('Element not found')
finally:
    print('Final')
