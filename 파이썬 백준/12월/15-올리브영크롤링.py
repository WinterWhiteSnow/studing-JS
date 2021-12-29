import requests
import sys
from bs4 import BeautifulSoup

url = "https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=100000100010008&fltDispCatNo=&prdSort=03&rowsPerPage=24&searchTypeSort=btn_thumb&plusButtonFlag=N&isLoginCnt=11&aShowCnt=1&bShowCnt=1&cShowCnt=1&trackingCd=Cat100000100010008_MID"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
page = soup.find("div",{"class":"pageing"}).find_all("a")[:-1]
pagenation = [int(i.text) for i in page]
last_page = pagenation[-1]
info = []
for i in range(1,last_page+1):
    URL = f"https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=100000100010008&fltDispCatNo=&prdSort=03&pageIdx={i}&rowsPerPage=48&searchTypeSort=btn_thumb&plusButtonFlag=N&isLoginCnt=13&aShowCnt=1&bShowCnt=1&cShowCnt=1&trackingCd=Cat100000100010008_Small"
    print(f"reading....{i}page")
    R = requests.get(URL)
    SOUP = BeautifulSoup(R.text,"html.parser")
    a = SOUP.find("div",{"id":"Contents"}).find_all("li")
    for b in a:
        c = b.find("div",{"class":"prd_name"})
        cl = b.find("div",{"class":"prd_info"})
        if c and cl:
            name = c.find("span",{"class":"tx_brand"}).text
            link = cl.find("a")["href"]
            wow = {
                "name":name,
                "link":link
            }
            info.append(wow)
            
for i in info:
    link = i["link"]
    r = requests.get(link)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,"html.parser")
        parent_tag = soup.find("ul",{"class":"prd_detail_tab"}).find("li",{"id":"reviewInfo"}).find("span").text
        review_num = int(parent_tag[1:-1].replace(",",""))
        i["review"]=review_num

wow = sorted(info, key = lambda x : x["review"],reverse=True)
result = []
for i in wow:
    print("to the edge")
    if i["review"] > 1000:
        result.append(i)
print(result)