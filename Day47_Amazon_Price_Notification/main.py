from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

URL = "https://www.amazon.ca/Instant-Pot-Duo-Multi-Use-Programmable/dp/B00FLYWNYQ"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                    "537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7"
}
response = requests.get(url=URL, headers=HEADERS)
pricer_tracker = response.text


soup = BeautifulSoup(pricer_tracker, "lxml")


product_price = float(soup.find(name="span", class_="a-offscreen").getText().strip("$"))
title = soup.find(id="productTitle").get_text().strip()
print(title)

# 當價格下跌至我想買的價格時，信箱會自動寄信給我，告訴我說可以買了
if product_price < 195:
    message = f"{title} is now {product_price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # 啟動安全傳輸系統
        result = connection.login("ewigwi@gmail.com", "eifnewignow")
        connection.sendmail(
            from_addr="ewigwi@gmail.com",
            to_addrs="lavouver96@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )