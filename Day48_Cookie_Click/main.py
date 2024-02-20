from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# configure setting
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--incognito')
options.add_argument("start-maximized")
options.add_experimental_option('detach', True)


def is_enough_money(current_money, buy_item):
  item = buy_item.text.split("-")[1].lstrip()
  money = current_money.text
  if ',' in item:
    item = ''.join(item.split(','))
  
  if ',' in money:
    money = ''.join(money.split(','))
  
  print(money, item)
  return int(money) >= int(item)

# choose browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# get into website
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# get the cookie
cookie = driver.find_element(by=By.ID, value='cookie')

# get all the id of upgraded items
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
items_id = [item.get_attribute("id") for item in items]


# set the time interval

endtime = time.time() + 60 * 5
entrytime = time.time()

# # float type
# print(endtime - time.time())


# check whether lasting for 5 minutes
while time.time() < endtime:
  cookie.click()

  # every 5 second, can buy an item
  if int(time.time() - entrytime) % 5 == 0:
    # Get all upgrade <b> tags
    all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
    # item_prices = []

    upgraded_detail = {}
    print(all_prices)
    # Get all upgraded price
    for idx, price in enumerate(all_prices):
      item_price = price.text
      
      if item_price:
        cost = int(item_price.split('-')[1].strip().replace(',', ''))
        # item_prices.append(cost)

      # Create upgraded detail: price and name
      upgraded_detail[items_id[idx]] = cost

    # Get the current money
    money = driver.find_element(by=By.ID, value="money").text
    if "," in money:
        money = money.replace(",", "")
    money = int(money)


    # find the most expensive item to buy
    # find the index of item can buy
    could_buy_item_idx = [i for i, c in enumerate(upgraded_detail.values()) if money >= c]


    # buy the most expensive item
    if len(could_buy_item_idx) > 0:
      buy_item = items_id[could_buy_item_idx[-1]]
      driver.find_element(by=By.ID, value=buy_item).click()


print(driver.find_element(by=By.ID, value="cps").text)










