from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import random
import time
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

wait = WebDriverWait(driver, 30)
driver.get("https://onecompiler.com/html/3zfhmhkem")
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div/div/div[1]/div[2]/div[1]/div/div[3]/button[3]'))).click()
time.sleep(10)
iframe = driver.find_element(By.XPATH, '//*[@id="ResultBrowserIframe"]')
driver.switch_to.frame(iframe)
if random.randint(0, 100) < 35:
  wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/ins'))).click()
time.sleep(30)
driver.quit()

