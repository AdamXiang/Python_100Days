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


driver.get("https://secure-retreat-92358.herokuapp.com/")

## Wiki Challenge
# count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")

# print(f'wikipedia has {count.text} articles in English.')

# # 透過抓取hyperlink的文字，我們可以直接做點選
# # 透過click，selenium會自動幫我們點擊此element
# today_articale = driver.find_element(by=By.LINK_TEXT, value='affine symmetric groups')
# today_articale.click()


# # 我們可以透過抓取form中的name，方便我們做文字輸入的操作
# # 使用下面的方法，可以讓我們按Enter進入搜尋結果
# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


# # Challenge
first_name = driver.find_element(by=By.NAME, value='fName')
last_name = driver.find_element(by=By.NAME, value='lName')
email = driver.find_element(by=By.NAME, value='email')
button = driver.find_element(by=By.CLASS_NAME, value='btn')

first_name.send_keys('Adam')
last_name.send_keys('Chang')
email.send_keys('alvegeonht@gmail.com')
button.send_keys(Keys.ENTER)