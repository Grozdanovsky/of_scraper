from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
chrome_options = Options()
chrome_options.add_argument('--log-level=1')
# chrome_options.add_argument('--headless')
chrome_path = which('chromedriver')
# s = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
driver.get('https://linktr.ee/lunnawtf')
button1 = driver.find_element(By.XPATH,"//button[contains(@class,'c-pFZIQ StyledButton-sc-686c3k-0')]")
button1.click()
button2 = driver.find_element(By.CLASS_NAME,"sc-pFZIQ.SensitiveContentUnlock__PrimaryButton-sc-1uk9vjj-0.fRlsIx.YJduB")
button2.click()
time.sleep(2)

allTabs = driver.window_handles

second_tab = driver.window_handles[1]
driver.switch_to.window(second_tab)
of_url = driver.current_url
print(of_url)

time.sleep(10000)

