import requests
from bs4 import BeautifulSoup

url = "https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}"
target_url = url.format(1)
r = requests.get(target_url)
soup = BeautifulSoup(r.text, "html.parser")
contents = soup.find_all("div", class_="cassetteitem")
content = contents[1]

detail = content.find("div", class_="cassetteitem-detail")
table = content.find("table", class_="cassetteitem_other")

title = detail.find("div", class_="cassetteitem_content-title").text
address = detail.find("li", class_="cassetteitem_detail-col1").text
access = detail.find("li", class_="cassetteitem_detail-col2").text
age = detail.find("li", class_="cassetteitem_detail-col3").text
tr_tags = table.find_all("tr", class_="js-cassette_link")
tr_tag = tr_tags[3]
tr_tag.find_all("td")[2:6]