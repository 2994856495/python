import urllib.request
from bs4 import BeautifulSoup
allHouse = []

url=  "https://bj.lianjia.com/ershoufang/rs%E6%B0%91%E6%97%8F%E5%A4%A7%E5%AD%A6/"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html.read().decode('utf-8'), "lxml")

data = soup.find_all("div", class_="info clear")   #返回满足条件的【所有】结果，通常用它
#data = soup.find("div", class_="info clear")        #返回满足条件的【第1个】结果
# print(data)                                            #可用word查字符数，对比这两个指令的结果

#quit()

for div1 in data:           #遍历所有div
    div11=div1.find("div", class_="title")          #继续细分，查找【class="title"】的div，这儿通常只有一个子div，可以不用find_all
    print(div11)
    # print(div11.a.string)       #

