import requests
import fake_useragent
from bs4 import BeautifulSoup
import re
#需求 名称|位置|屋型|面积|单价|总价
def getHTMLText(url):
    try:
        headers = {"user-agent": fake_useragent.UserAgent().chrome}
        r = requests.get(url, timeout=30,headers=headers)
        r.raise_for_status() #如果状态不是200，引发异常
        r.encoding = 'utf-8' #无论原来用什么编码，都改成utf-8
        return r.text
    except:
        print(r)
        print("error,unexpected")
        return ""


url = r"https://bj.5i5j.com/ershoufang/_%E6%B0%91%E6%97%8F%E5%A4%A7%E5%AD%A6?zn=%E6%B0%91%E6%97%8F%E5%A4%A7%E5%AD%A6"
html = getHTMLText(url)
soup = BeautifulSoup(html, "lxml")#PARSER = lxml
print(soup)