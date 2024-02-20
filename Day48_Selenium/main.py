from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# webdriver.ChromeOptions

# configure setting
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--incognito')
options.add_argument("start-maximized")
options.add_experimental_option('detach', True)

# choose browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# control window size    driver.maximize_window()

driver.get("https://www.python.org/")


# Amazon Price Search
# shoe_price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")

# print(f"price of nike shoe is: {shoe_price.text} dollars.")

upcoming_events = {}

list_events = driver.find_elements(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

for idx, event in enumerate(list_events):
  dt, et = event.text.split(maxsplit=1)
  upcoming_events[idx] = {'time': dt, 'name': et}


print(upcoming_events) 

# close會關閉單一特別的tab
time.sleep(10)
# driver.close()
# quit會關閉一整個網頁
driver.quit()