from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
y_website = response.text

soup = BeautifulSoup(y_website, "html.parser")
article = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for text in article:
    article_text = text.getText()
    article_texts.append(article_text)
    article_link = text.get("href")
    article_links.append(article_link)
# article_text = soup.select_one(".titlelink").text  我的方法找到第一個標題

article_score = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_score = max(article_score)
largest_index = article_score.index(largest_score)
print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_index)
# index = 0
# max_score = article_score[index]
# for score in article_score:
#     if score > max_score:
#         max_score = score
#         index = article_score.index(max_score)
#
# print(article_links[index])
# print(article_texts[index])






















# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # soup.title.string 可以給你title的句子
# # prettify可以讓tag有indent
# print(soup.prettify())
#
# # find_all 可以幫我們找到html 中所有的 a tag
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     # print(tag.getText()) 可以拿到 tag 中的文字
#     # get() 裡面可以放入 tag 的 attribute
#     print(tag.get("href"))
#
# # 透過 find() 抓出其中的tag： name 代表 tag 的名字， id 代表 tag 中的 id
# heading = soup.find(name="h1", id="name")
# # class 是保留字，若要抓取tag中的class要使用class_
# heading2 = soup.find(name="h3", class_="heading")
# # 若我們想抓出nested tag的話，可以使用select and select_one，兩者差別在於只抓第一個跟全抓，並使用CSS-selector，就可抓取
# # 抓 id = name 的 tag
# name = soup.select_one(select="#name")
# pa = soup.select_one(select="p a")
# print(pa)