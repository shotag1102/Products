import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

url = "https://www.jalan.net/270000/LRG_272000/?stayYear=&stayMonth=&stayDay=&dateUndecided=1&stayCount=1&roomCount=1&adultNum=2&ypFlg=1&kenCd=270000&screenId=UWW1380&roomCrack=200000&lrgCd=272000&distCd=01&rootCd=04/page{}#"
d_list = []
for i in range(1,4):
    target_url = url.format(i)
    r = requests.get(target_url)

    sleep(1)

    soup = BeautifulSoup(r.content, "html.parser")

    products = soup.find_all("div", class_="p-yadoCassette__body p-searchResultItem__body")
    for product in products:
        row = product.find("div", class_="p-yadoCassette__summary p-searchResultItem__summary")
        table = product.find("table", class_="p-planTable p-searchResultItem__planTable")

        name = row.find("h2", class_="p-searchResultItem__facilityName").text

        if table is None:
            pass
        else:
            tr_tags = table.find_all("tr")[1:3]
            for tr_tag in tr_tags:
                if len(tr_tag.find_all("td"))<3:
                    pass
                else:
                    point_info,per,total = tr_tag.find_all("td")
                    point = point_info.find("li", class_="c-label c-label--orange p-searchResultItem__horizontalLabel overwritePointLabel")
                    perfee = per.find("span")
                    totalfee = total.find("span")
                    if point is None:
                        pass
                    else:
                        d = {
                        "name":name,
                        "point":point.text,
                        "perfee":perfee.text,
                        "totalfee":totalfee.text
                        }
                        d_list.append(d)
                        df = pd.DataFrame(d_list)
                        df.to_csv("test.csv", index=None,encoding="utf-8-sig")
